"""Small same-domain feature-transfer experiment; no pretrained download."""
import importlib.util
import json
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def main():
    path=Path(__file__).resolve().parents[1]/'projects/intermediate/digits-cnn/train.py'
    spec=importlib.util.spec_from_file_location('cnn',path);cnn=importlib.util.module_from_spec(spec);spec.loader.exec_module(cnn)
    X,y,train,valid,test=cnn.split_data()
    # Source labels 0..4, target labels 5..9; source sees no target training/test images.
    source_train=train[y[train]<5];source_valid=valid[y[valid]<5]
    p,_,_=cnn.fit(X[source_train],y[source_train],X[source_valid],y[source_valid],epochs=8)
    target_train=train[y[train]>=5];target_test=test[y[test]>=5]
    a=cnn.forward(X[target_train],p)[1][2];b=cnn.forward(X[target_test],p)[1][2]
    head=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000)).fit(a,y[target_train])
    raw=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000)).fit(X[target_train].reshape(len(target_train),-1),y[target_train])
    report={'source_train_rows':len(source_train),'target_train_rows':len(target_train),'target_test_rows':len(target_test),
            'frozen_feature_accuracy':float(accuracy_score(y[target_test],head.predict(b))),
            'raw_pixel_accuracy':float(accuracy_score(y[target_test],raw.predict(X[target_test].reshape(len(target_test),-1)))),
            'scope':'same-domain digit-label transfer; not a pretrained large-model benchmark'}
    output=Path('outputs');output.mkdir(exist_ok=True)
    np.savez(output/'source-convolution.npz',**p)
    loaded=dict(np.load(output/'source-convolution.npz',allow_pickle=False))
    np.testing.assert_allclose(cnn.forward(X[target_test],loaded)[0],cnn.forward(X[target_test],p)[0])
    (output/'transfer.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps(report,indent=2))


if __name__=='__main__':main()
