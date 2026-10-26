"""Offline examples and integrated course-mentor capstone."""
import argparse
import json
from pathlib import Path
from .agent import run_plan
from .automation import Queue
from .llm import MockLLM,Gemini
from .rag import Retriever,evaluate
from .repairs import image_lab


def main():
    parser=argparse.ArgumentParser();parser.add_argument('case',choices=['assistant','rag','agent','automation','capstone','images']);parser.add_argument('--live',action='store_true');args=parser.parse_args()
    if args.live and args.case!='assistant':parser.error('--live is only available for assistant')
    if args.case=='assistant':
        provider=Gemini() if args.live else MockLLM()
        value={'mode':'live' if args.live else 'mock','result':provider.generate('Explain training-only preprocessing. Return answer and citations JSON.')}
    elif args.case=='rag':value=evaluate()
    elif args.case=='agent':value=run_plan([{'tool':'search','query':'validation checkpoint'},{'tool':'answer','query':'validation checkpoint'}])
    elif args.case=='automation':
        q=Queue();q.add('lesson-1','2026-10-27T09:00:00+05:30',{'lesson':'Python'})
        value={'first':q.dry_run('2026-10-27T04:00:00Z'),'repeat':q.dry_run('2026-10-27T04:00:00Z')};q.close()
    elif args.case=='images':value=image_lab()
    else:
        q=Queue();answer=Retriever().answer('How do I practice Python loops?')
        trace=run_plan([{'tool':'answer','query':'How do I practice Python loops?'},
                        {'tool':'propose_message','query':'Draft: review the Python exercise.'}])
        q.add('mentor-1','2026-10-27T04:00:00Z',{'exercise':'PY-011','answer_citations':answer['citations']})
        value={'answer':answer,'workflow':trace,'simulation':q.dry_run('2026-10-27T05:00:00Z')};q.close()
    output=Path('outputs');output.mkdir(exist_ok=True)
    (output/f'{args.case}.json').write_text(json.dumps(value,indent=2,allow_nan=False),encoding='utf-8')
    print(json.dumps(value,indent=2,allow_nan=False))


if __name__=='__main__':main()
