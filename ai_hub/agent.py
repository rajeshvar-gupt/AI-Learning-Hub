"""Bounded plan/execute/review runner with supplied plans; no autonomous LLM planner."""
from .rag import Retriever


def run_plan(plan,max_steps=4,retriever=None):
    if isinstance(max_steps,bool) or not isinstance(max_steps,int) or not 1<=max_steps<=8:
        raise ValueError('max_steps must be 1..8')
    if not isinstance(plan,list) or not plan or len(plan)>max_steps:
        raise ValueError('nonempty plan exceeds step budget')
    r=Retriever() if retriever is None else retriever
    trace=[]
    for step in plan:
        if not isinstance(step,dict) or set(step)!={'tool','query'} or not isinstance(step['query'],str) or not 0<len(step['query'])<=2000:
            raise ValueError('step requires tool and bounded query')
        if step['tool'] not in ['search','answer','propose_message']:
            raise ValueError('tool outside allowlist')
        try:
            if step['tool']=='propose_message':
                result={'status':'awaiting_human_approval','draft':step['query'],'sent':False}
            elif step['tool']=='search':result=r.search(step['query'])
            else:result=r.answer(step['query'])
            trace.append({'tool':step['tool'],'state':'reviewed','result':result})
        except (ValueError,RuntimeError) as error:
            trace.append({'tool':step['tool'],'state':'failed','error':type(error).__name__})
            break
    return {'steps':len(trace),'trace':trace,'completed':len(trace)==len(plan) and all(x['state']=='reviewed' for x in trace)}
