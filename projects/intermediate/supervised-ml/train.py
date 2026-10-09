"""Train-only CV selection; one final holdout report per task."""
import json
import platform
from pathlib import Path
import numpy as np
import sklearn
from sklearn.datasets import load_iris, make_regression
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             mean_absolute_error, r2_score, root_mean_squared_error)
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

SEED = 42


def regression_data():
    X, y = make_regression(n_samples=320, n_features=6, n_informative=4,
                           noise=12, random_state=SEED)
    return train_test_split(X, y, test_size=.25, random_state=SEED)


def classification_data():
    X, y = load_iris(return_X_y=True)
    return train_test_split(X, y, test_size=.25, stratify=y, random_state=SEED)


def pipeline(model):
    return Pipeline([("impute", SimpleImputer(strategy="median")),
                     ("scale", StandardScaler()), ("model", model)])


def choose(X, y, task):
    if task == "regression":
        candidates = [
            ("mean_baseline", DummyRegressor(), {}),
            ("ridge", Ridge(), {"model__alpha": [.1, 1., 10.]}),
            ("forest", RandomForestRegressor(n_estimators=60, random_state=SEED, n_jobs=1),
             {"model__max_depth": [3, None]}),
        ]
        cv = KFold(5, shuffle=True, random_state=SEED)
        scoring = "neg_mean_absolute_error"
    elif task == "classification":
        candidates = [
            ("majority_baseline", DummyClassifier(strategy="most_frequent"), {}),
            ("logistic", LogisticRegression(max_iter=1000), {"model__C": [.1, 1., 10.]}),
            ("tree", DecisionTreeClassifier(random_state=SEED), {"model__max_depth": [2, 4]}),
            ("forest", RandomForestClassifier(n_estimators=60, random_state=SEED, n_jobs=1),
             {"model__max_depth": [2, None]}),
            ("knn", KNeighborsClassifier(), {"model__n_neighbors": [3, 7]}),
            ("svm", SVC(), {"model__C": [.1, 1., 10.]}),
            ("naive_bayes", GaussianNB(), {}),
        ]
        cv = StratifiedKFold(5, shuffle=True, random_state=SEED)
        scoring = "f1_macro"
    else:
        raise ValueError("unknown task")
    rows, winner, best_score = [], None, -np.inf
    baseline = None
    for name, model, grid in candidates:
        search = GridSearchCV(pipeline(model), grid, scoring=scoring, cv=cv,
                              n_jobs=1, error_score="raise")
        search.fit(X, y)  # No holdout data enters this function.
        row = dict(name=name, cv_score=float(search.best_score_),
                   cv_std=float(search.cv_results_["std_test_score"][search.best_index_]),
                   params=search.best_params_)
        rows.append(row)
        if name.endswith("baseline"):
            baseline = search.best_estimator_
        if search.best_score_ > best_score:
            best_score = search.best_score_
            winner = (name, search.best_estimator_)
    return winner, baseline, rows, scoring


def evaluate(task):
    X_train, X_test, y_train, y_test = (regression_data() if task == "regression" else classification_data())
    (name, fitted), baseline, rows, scoring = choose(X_train, y_train, task)
    # Selection is frozen before either holdout prediction.
    predictions = fitted.predict(X_test)
    base_predictions = baseline.predict(X_test)
    def metrics(pred):
        if task == "regression":
            return dict(mae=float(mean_absolute_error(y_test, pred)),
                        rmse=float(root_mean_squared_error(y_test, pred)),
                        r2=float(r2_score(y_test, pred)))
        return dict(accuracy=float(accuracy_score(y_test, pred)),
                    macro_f1=float(f1_score(y_test, pred, average="macro", zero_division=0)),
                    confusion_matrix=confusion_matrix(y_test, pred, labels=[0, 1, 2]).tolist(),
                    label_order=load_iris().target_names.tolist())
    return dict(task=task, seed=SEED, train_rows=len(y_train), test_rows=len(y_test),
                cv_folds=5, selection_scoring=scoring, candidates=rows, selected=name,
                baseline_test=metrics(base_predictions), selected_test=metrics(predictions))


def main():
    report = dict(environment=dict(python=platform.python_version(), numpy=np.__version__,
                                   sklearn=sklearn.__version__),
                  regression=evaluate("regression"), classification=evaluate("classification"))
    output = Path(__file__).parent / "outputs"
    output.mkdir(exist_ok=True)
    (output / "report.json").write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
