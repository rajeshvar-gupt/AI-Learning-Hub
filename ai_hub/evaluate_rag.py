"""Frozen external-label retrieval evaluation; not generated-answer quality."""
import hashlib
import json
from pathlib import Path
import urllib.request
import numpy as np
from .rag import Retriever

COMMIT='eee5fdbf62f8613a7812b03419e6b29617b74fd1'
GIT_BLOB='e9a3f913ad1468ebe105b891334ca7b0bc0e2510'
URL=f'https://raw.githubusercontent.com/rajpurkar/SQuAD-explorer/{COMMIT}/dataset/dev-v1.1.json'


def verify_bytes(data):
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if blob!=GIT_BLOB:raise ValueError('dataset does not match pinned upstream Git blob')
    return hashlib.sha256(data).hexdigest()


def select_cases(dataset):
    # Protocol fixed before observing scores. No relevance-based sampling.
    documents=[];cases=[]
    for ai,article in enumerate(dataset['data'][:20]):
        for pi,paragraph in enumerate(article['paragraphs'][:2]):
            identifier=f'article-{ai}-paragraph-{pi}'
            documents.append({'id':identifier,'text':paragraph['context']})
            for qa in paragraph['qas'][:2]:
                if not qa.get('answers'):raise ValueError('SQuAD 1.1 answerable case required')
                cases.append({'id':qa['id'],'query':qa['question'],'document':identifier,
                              'answers':[a['text'] for a in qa['answers']]})
    if not documents or not cases:raise ValueError('empty evaluation selection')
    return documents,cases


def score(documents,cases):
    retriever=Retriever(documents);rows=[]
    analyze=retriever.vectorizer.build_analyzer()
    for case in cases:
        hits=retriever.search(case['query'],k=5)
        terms=set(analyze(case['query']))
        keyword=sorted(retriever.chunks,key=lambda d:(-len(terms & set(analyze(d['text']))),d['id']))[:5]
        ranks=[i+1 for i,h in enumerate(hits) if h['document']==case['document']]
        rank=min(ranks) if ranks else None
        # This tests gold-span availability in retrieved text, not generated-answer correctness.
        available=any(a.casefold() in h['text'].casefold() for h in hits[:2] for a in case['answers'])
        rows.append({'id':case['id'],'expected_document':case['document'],
                     'retrieved_chunk_ids':[h['id'] for h in hits],
                     'first_relevant_chunk_rank':rank,'gold_span_available_at_2':available,
                     'keyword_document_hit_at_2':case['document'] in [h['document'] for h in keyword[:2]]})
    def recall(k):return float(np.mean([r['first_relevant_chunk_rank'] is not None and r['first_relevant_chunk_rank']<=k for r in rows]))
    return {'documents':len(documents),'chunks':len(retriever.chunks),'questions':len(cases),
            'document_recall_at_1':recall(1),'document_recall_at_2':recall(2),'document_recall_at_5':recall(5),
            'mrr_at_5':float(np.mean([1/r['first_relevant_chunk_rank'] if r['first_relevant_chunk_rank'] else 0 for r in rows])),
            'gold_span_available_at_2':float(np.mean([r['gold_span_available_at_2'] for r in rows])),
            'keyword_document_recall_at_2':float(np.mean([r['keyword_document_hit_at_2'] for r in rows])),
            'cases':rows}


def main():
    output=Path('outputs/external-rag');output.mkdir(parents=True,exist_ok=True)
    # Runtime cache is ignored by git; no source paragraphs/questions are redistributed.
    path=output/'dev-v1.1.json'
    if path.exists():data=path.read_bytes()
    else:
        with urllib.request.urlopen(URL,timeout=30) as response:data=response.read(10_000_001)
        if len(data)>10_000_000:raise ValueError('dataset exceeds size budget')
        verify_bytes(data);path.write_bytes(data)
    sha=verify_bytes(data)
    documents,cases=select_cases(json.loads(data))
    report={'dataset':'SQuAD 1.1 development set','upstream_commit':COMMIT,'git_blob':GIT_BLOB,
            'source_url':URL,'sha256':sha,'license':'CC BY-SA 4.0',
            'protocol':'first 20 articles; first 2 paragraphs/article; first 2 questions/paragraph; no tuning',
            'scope':'external English encyclopedia QA retrieval; not representative of private course support or a generated-answer benchmark',
            **score(documents,cases)}
    (output/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
