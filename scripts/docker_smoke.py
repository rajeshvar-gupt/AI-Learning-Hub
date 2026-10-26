"""Build and smoke-test the teaching image; remove only the container we create."""
import json
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.request

ROOT=Path(__file__).resolve().parents[1]


def command(*args):
    return subprocess.check_output(list(args),cwd=ROOT,text=True).strip()


def request(base,path,payload=None):
    body=None if payload is None else json.dumps(payload).encode()
    req=urllib.request.Request(base+path,data=body,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=3) as response:
        return response.status,json.load(response)


def main():
    subprocess.run(['docker','build','--tag','ai-learning-hub:ci','.'],cwd=ROOT,check=True)
    cid=command('docker','run','--detach','--rm','--read-only','--tmpfs','/tmp:rw,noexec,nosuid,size=64m',
                '--cap-drop','ALL','--security-opt','no-new-privileges','--pids-limit','100',
                '--publish','127.0.0.1::8000','ai-learning-hub:ci')
    try:
        info=json.loads(command('docker','inspect',cid))[0]
        if info['Config']['User'] in ['', '0', 'root']:raise AssertionError('container must run non-root')
        port=info['NetworkSettings']['Ports']['8000/tcp'][0]['HostPort']
        base='http://127.0.0.1:'+port
        deadline=time.monotonic()+60
        while True:
            try:
                status,health=request(base,'/health')
                if status==200 and health['status']=='ok':break
            except (urllib.error.URLError,TimeoutError,ConnectionError):pass
            if time.monotonic()>deadline:raise AssertionError('container health deadline exceeded')
            time.sleep(.5)
        status,pred=request(base,'/predict',{'samples':[[5.1,3.5,1.4,.2]]})
        assert status==200 and pred['labels']==['setosa']
        for payload in [{'samples':[[True,2,3,4]]},{'samples':[]},{'wrong':1}]:
            try:request(base,'/predict',payload)
            except urllib.error.HTTPError as error:assert error.code==422
            else:raise AssertionError('invalid request was accepted')
        # Also execute the actual image healthcheck command, not just the host request.
        check=info['Config']['Healthcheck']['Test']
        if check[0]!='CMD':raise AssertionError('expected exec healthcheck')
        subprocess.run(['docker','exec',cid,*check[1:]],check=True,cwd=ROOT)
        print(json.dumps({'image':'ai-learning-hub:ci','nonroot_user':info['Config']['User'],
                          'health':'passed','prediction':'setosa','invalid_inputs':'rejected',
                          'container_healthcheck':'passed','public_deployment':False},indent=2))
    finally:
        # Exact ID obtained from this invocation; no prune or broad deletion.
        subprocess.run(['docker','stop','--time','5',cid],cwd=ROOT,check=False)


if __name__=='__main__':main()
