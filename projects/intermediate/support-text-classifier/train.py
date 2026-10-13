"""Offline TF-IDF classification with train-only CV on original invented text."""
import json
from pathlib import Path
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline


def dataset():
    """Fixed instructional partitions; no customer or student records."""
    train = {
        'billing': [
            'Please explain the invoice charges', 'My payment was deducted twice',
            'I need a refund for the cancelled order', 'Where can I download the receipt',
            'The card payment failed at checkout', 'Why is the invoice amount wrong',
            'Please confirm the refund status', 'I was charged after cancellation',
            'Can I pay the course fee in installments', 'The receipt shows a duplicate charge',
            'I need help with a declined payment', 'Please update the billing address on my invoice'],
        'access': [
            'I cannot login to my account', 'Please reset my password',
            'The verification code never arrived', 'My account is locked',
            'The sign in page rejects my email', 'I forgot my login credentials',
            'The password reset link has expired', 'I cannot access the student portal',
            'Please unlock my account', 'The login code is invalid',
            'My sign in session keeps expiring', 'I need to change my account password'],
        'course': [
            'Where are the Python lesson notes', 'When is the next live class',
            'Please share the assignment deadline', 'I need the lecture recording',
            'Which lessons cover machine learning', 'How do I submit the course project',
            'Please explain the quiz question', 'Can you send the class schedule',
            'The lesson video has no subtitles', 'Where can I find the practice exercises',
            'I need feedback on my assignment', 'Please share the syllabus and lecture slides']}
    test = {
        'billing': ['The invoice includes an extra charge', 'Has my refund been issued',
                    'Can you resend the payment receipt', 'I want to dispute this card charge'],
        'access': ['My login is blocked after a password change', 'I cannot use the expired reset link',
                   'Please help me access my locked account', 'No verification code reached my email'],
        'course': ['Where is the recording of the last class', 'Please clarify the project deadline',
                   'Can I see the lesson slides', 'I have a question about the practice quiz']}
    def flatten(part):
        pairs = [(text, label) for label in sorted(part) for text in part[label]]
        return [x[0] for x in pairs], np.array([x[1] for x in pairs])
    return (*flatten(train), *flatten(test))


def validate_texts(texts):
    if isinstance(texts, str):
        raise ValueError('pass a nonempty list of texts, not one string')
    texts = list(texts)
    if not texts or any(not isinstance(x, str) or not x.strip() for x in texts):
        raise ValueError('each text must be a nonblank string')
    return texts


def select_model(texts, labels):
    texts = validate_texts(texts)
    labels = np.asarray(labels)
    if labels.shape != (len(texts),):
        raise ValueError('one label per training text required')
    classes, counts = np.unique(labels, return_counts=True)
    if len(classes) < 2 or counts.min() < 3:
        raise ValueError('at least two classes with three examples each required')
    model = Pipeline([
        ('tfidf', TfidfVectorizer(lowercase=True, stop_words=None)),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))])
    search = GridSearchCV(model,
                          {'tfidf__ngram_range': [(1, 1), (1, 2)],
                           'classifier__C': [.5, 2.]},
                          scoring='f1_macro', cv=StratifiedKFold(3, shuffle=True, random_state=42),
                          error_score='raise', n_jobs=1)
    search.fit(texts, labels)  # Vocabulary and IDF are fitted inside each training fold.
    return search


def route(model, texts):
    texts = validate_texts(texts)
    features = model.named_steps['tfidf'].transform(texts)
    predictions = model.named_steps['classifier'].predict(features)
    return [dict(text=text, predicted=str(pred), route=str(pred) if row.nnz else 'needs_review',
                 known_features=int(row.nnz))
            for text, pred, row in zip(texts, predictions, features)]


def main():
    train_text, y_train, test_text, y_test = dataset()
    search = select_model(train_text, y_train)
    selected = search.best_estimator_
    pred = selected.predict(test_text)
    baseline = DummyClassifier(strategy='most_frequent').fit(np.zeros((len(y_train), 1)), y_train)
    base_pred = baseline.predict(np.zeros((len(y_test), 1)))
    classes = selected.classes_.tolist()
    def metrics(labels):
        return dict(accuracy=float(accuracy_score(y_test, labels)),
                    macro_f1=float(f1_score(y_test, labels, average='macro', zero_division=0)))
    candidates = [dict(params=params, mean_macro_f1=float(mean), std_macro_f1=float(std))
                  for params, mean, std in zip(search.cv_results_['params'],
                                               search.cv_results_['mean_test_score'],
                                               search.cv_results_['std_test_score'])]
    report = dict(seed=42, origin='original invented instructional examples',
                  train_rows=len(y_train), test_rows=len(y_test), cv_folds=3,
                  best_params=search.best_params_, candidates=candidates,
                  vocabulary_size=len(selected.named_steps['tfidf'].vocabulary_),
                  baseline_test=metrics(base_pred), selected_test=metrics(pred),
                  label_order=classes,
                  confusion_matrix=confusion_matrix(y_test, pred, labels=classes).tolist(),
                  per_class=classification_report(y_test, pred, labels=classes, output_dict=True, zero_division=0),
                  test_predictions=[dict(text=t, actual=str(y), predicted=str(p))
                                    for t,y,p in zip(test_text, y_test, pred)],
                  example_routes=route(selected, ['Please help me reset my password', 'zzzzunseenword']))
    output = Path(__file__).parent/'outputs'
    output.mkdir(exist_ok=True)
    (output/'report.json').write_text(json.dumps(report, indent=2, allow_nan=False), encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['per_class','test_predictions','candidates']}, indent=2))


if __name__ == '__main__':
    main()
