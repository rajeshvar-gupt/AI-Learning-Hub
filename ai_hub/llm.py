"""Mockable Gemini REST adapter with bounded retries and application validation."""
import json
import os
import re
import time
import urllib.error
import urllib.request

SCHEMA = {'type':'object','properties':{'answer':{'type':'string'},
          'citations':{'type':'array','items':{'type':'string'}}},
          'required':['answer','citations']}


def validate_answer(value, allowed_ids=None):
    if not isinstance(value, dict) or set(value) != {'answer','citations'}:
        raise ValueError('answer and citations fields required')
    if not isinstance(value['answer'], str) or not value['answer'].strip():
        raise ValueError('nonblank answer required')
    ids=value['citations']
    if not isinstance(ids,list) or any(not isinstance(x,str) or not x for x in ids):
        raise ValueError('citation IDs must be nonempty strings')
    if len(set(ids))!=len(ids):
        raise ValueError('duplicate citation IDs')
    if allowed_ids is not None and not set(ids).issubset(set(allowed_ids)):
        raise ValueError('unknown citation ID')
    return value


def post_json(url, body, headers):
    request=urllib.request.Request(url,data=json.dumps(body).encode(),headers=headers,method='POST')
    with urllib.request.urlopen(request,timeout=15) as response:
        return json.load(response)


class Gemini:
    def __init__(self, key=None, model=None, transport=post_json, sleeper=time.sleep, attempts=3):
        self.key=key if key is not None else os.getenv('GEMINI_API_KEY','')
        self.model=model if model is not None else os.getenv('GEMINI_MODEL','')
        if not self.key or not re.fullmatch(r'[A-Za-z0-9._-]+',self.model):
            raise ValueError('set GEMINI_API_KEY and a valid GEMINI_MODEL ID')
        if isinstance(attempts,bool) or not isinstance(attempts,int) or not 1<=attempts<=3:
            raise ValueError('attempts must be 1..3')
        self.transport,self.sleeper,self.attempts=transport,sleeper,attempts

    def generate(self, prompt):
        if not isinstance(prompt,str) or not prompt.strip() or len(prompt)>20000:
            raise ValueError('prompt must contain 1..20000 characters')
        body={'contents':[{'parts':[{'text':prompt}]}],
              'generationConfig':{'responseMimeType':'application/json',
                                  'responseSchema':SCHEMA,'maxOutputTokens':512}}
        url=f'https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent'
        for attempt in range(self.attempts):
            try:
                response=self.transport(url,body,{'Content-Type':'application/json','x-goog-api-key':self.key})
                candidate=response['candidates'][0]
                if candidate.get('finishReason')!='STOP':
                    raise ValueError('incomplete or blocked provider output')
                raw=''.join(p.get('text','') for p in candidate['content']['parts'])
                return validate_answer(json.loads(raw))
            except urllib.error.HTTPError as error:
                if error.code not in [429,500,502,503,504] or attempt+1==self.attempts:
                    raise RuntimeError(f'provider HTTP {error.code}') from None
                self.sleeper(.1*2**attempt)
            except (KeyError,IndexError,TypeError,json.JSONDecodeError) as error:
                raise ValueError('malformed provider response') from error
            except (urllib.error.URLError,TimeoutError):
                raise RuntimeError('provider connection failed; no automatic retry') from None


class MockLLM:
    """Fixture responses test integration, not LLM quality."""
    def generate(self,prompt):
        return {'answer':'Mock explanation: use a training split before fitting preprocessing.', 'citations':[]}
