import pandas as pd
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import yaml
from sklearn.model_selection import train_test_split
from .data import process_data


# Optional: implement hyperparameter tuning.
def train_model(X_train: np.array, y_train: np.array) -> RandomForestClassifier:
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model


def compute_model_metrics(y: np.array, preds: np.array) -> (float, float, float):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model: RandomForestClassifier, X: np.array) -> np.array:
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : RandomForestClassifier
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


def get_model_performance_on_slice(data: pd.DataFrame, sclice_columns: list = None):
    with open("../config.yml") as fp:
        model_config = yaml.load(fp, Loader=yaml.FullLoader)["modeling"]

    # split dataset on train and test parts
    if sclice_columns is not None:
        data = data[sclice_columns]
    train_data, test_data = train_test_split(data, test_size=model_config["test_size"], random_state=43)

    # preprocess training dataset
    X_train, y_train, encoder, lb = process_data(
        X=train_data,
        categorical_features=model_config["categorical_fature_names"],
        label=model_config["target_feature_name"],
        training=True,
    )

    # fit model
    model = train_model(X_train, y_train)

    # inference on test dataset
    X_test, y_test, _, _ = process_data(
        X=train_data,
        categorical_features=model_config["categorical_fature_names"],
        label=model_config["target_feature_name"],
        training=False,
    )

    test_preds = inference(model, X_test)
    return compute_model_metrics(y_test, test_preds)
