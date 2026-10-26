"""Local teaching HTTP API; trusted JSON model parameters, no pickle loading."""
import argparse
import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import numpy as np
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def train(path):
    data=load_iris();X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,test_size=.25,stratify=data.target,random_state=42)
    scaler=StandardScaler().fit(X_train)
    model=LogisticRegression(max_iter=1000).fit(scaler.transform(X_train),y_train)
    pred=model.predict(scaler.transform(X_test))
    dummy=DummyClassifier(strategy='most_frequent').fit(X_train,y_train)
    artifact={'schema_version':1,'mean':scaler.mean_.tolist(),'scale':scaler.scale_.tolist(),
              'coef':model.coef_.tolist(),'intercept':model.intercept_.tolist(),
              'classes':data.target_names.tolist(), 'feature_order':data.feature_names,
              'metrics':{'test_rows':len(y_test),'accuracy':float(accuracy_score(y_test,pred)),
                         'macro_f1':float(f1_score(y_test,pred,average='macro')),
                         'baseline_accuracy':float(accuracy_score(y_test,dummy.predict(X_test)))}}
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(artifact,indent=2,allow_nan=False),encoding='utf-8')
    loaded=load_model(path)
    if not np.array_equal(np.argmax(predict(loaded,X_test.tolist())['probabilities'],axis=1),pred):
        raise AssertionError('JSON reload predictions differ')
    return artifact


def load_model(path):
    a=json.loads(Path(path).read_text(encoding='utf-8'))
    if a.get('schema_version')!=1 or len(a.get('classes',[]))!=3:raise ValueError('unsupported model schema')
    for key,shape in [('mean',(4,)),('scale',(4,)),('coef',(3,4)),('intercept',(3,))]:
        value=np.asarray(a[key],dtype=float)
        if value.shape!=shape or not np.isfinite(value).all():raise ValueError('invalid model arrays')
    if np.any(np.asarray(a['scale'])<=0):raise ValueError('positive scales required')
    return a


def predict(model,samples):
    if not isinstance(samples,list) or not 1<=len(samples)<=100:raise ValueError('1..100 rows required')
    for row in samples:
        if not isinstance(row,list) or len(row)!=4 or any(isinstance(x,bool) or not isinstance(x,(int,float)) or not np.isfinite(x) or x<=0 or x>100 for x in row):
            raise ValueError('four positive finite measurements in cm, each <=100, required')
    X=(np.array(samples)-model['mean'])/model['scale']
    logits=X @ np.array(model['coef']).T+model['intercept']
    scores=np.exp(logits-logits.max(axis=1,keepdims=True));prob=scores/scores.sum(axis=1,keepdims=True)
    return {'labels':[model['classes'][i] for i in prob.argmax(axis=1)],'probabilities':prob.tolist()}


def make_server(model,host='127.0.0.1',port=8000):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def reply(self,status,value):
            body=json.dumps(value,allow_nan=False).encode();self.send_response(status)
            self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
        def do_GET(self):
            self.reply(200,{'status':'ok','schema_version':1}) if self.path=='/health' else self.reply(404,{'error':'not found'})
        def do_POST(self):
            if self.path!='/predict':return self.reply(404,{'error':'not found'})
            try:
                length=int(self.headers.get('Content-Length','0'))
                if not 0<length<=8192:return self.reply(413,{'error':'body size must be 1..8192 bytes'})
                value=json.loads(self.rfile.read(length))
                if not isinstance(value,dict) or set(value)!={'samples'}:raise ValueError('samples field required')
                return self.reply(200,predict(model,value['samples']))
            except (ValueError,TypeError,OverflowError):return self.reply(422,{'error':'invalid prediction input'})
    return ThreadingHTTPServer((host,port),Handler)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['train','serve']);parser.add_argument('--model',default='outputs/iris/model.json');parser.add_argument('--host',default='127.0.0.1');parser.add_argument('--port',type=int,default=8000);args=parser.parse_args()
    if args.command=='train':print(json.dumps(train(args.model)['metrics'],indent=2))
    else:
        server=make_server(load_model(args.model),args.host,args.port)
        try:server.serve_forever()
        finally:server.server_close()


if __name__=='__main__':main()
