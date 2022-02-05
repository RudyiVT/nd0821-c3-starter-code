import numpy as np
from sklearn.ensemble import RandomForestClassifier
from starter.starter.ml.model import train_model, compute_model_metrics, inference


def test_train_model():
    # testing train_model function
    X = np.array([[0, 1, 0, 2], [3, 5, 10, 2]])
    y = np.array(['a', 'b'])
    model = train_model(X, y)
    assert type(model) == RandomForestClassifier


def test_compute_model_metrics():
    # testing compute_model_metrics function
    y = [1, 0, 1]
    preds = [1, 0, 1]
    assert compute_model_metrics(y, preds) == (1, 1, 1)


def test_inference():
    # testing inference function
    X = np.array([[0, 1, 0, 2], [3, 5, 10, 2]])
    y = np.array(['a', 'b'])
    model = train_model(X, y)

    X_train = np.array([[0, 1, 0, 2], [3, 5, 10, 2]])
    y_train = np.array(['a', 'b'])
    model = train_model(X_train, y_train)

    X_test = np.array([[-1, 3, 8, 2], [4, 2, 0, 3]])

    preds = inference(model, X_test)

    assert (preds == np.array(['a', 'a'])).all()
