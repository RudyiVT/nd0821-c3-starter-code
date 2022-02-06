# Script to train machine learning model.
import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import pickle

from ml.data import process_data
from ml.model import train_model


if __name__ == "__main__":
    # Load cleaned dataset
    data = pd.read_csv("../data/census_cleaned.csv")

    # Load configs for training pipeline
    with open("../config.yml") as fp:
        model_config = yaml.load(fp, Loader=yaml.FullLoader)["modeling"]

    # split dataset on train and test parts
    train_data, test_data = train_test_split(data, test_size=model_config["test_size"])

    # preprocess training dataset
    X_train, y_train, encoder, lb = process_data(
        X=train_data,
        categorical_features=model_config["categorical_fature_names"],
        label=model_config["target_feature_name"],
        training=True,
    )

    # fit model
    model = train_model(X_train, y_train)

    # save model and encoders
    with open("../model/model.pkl", 'wb') as fp:
        model_arfitact = {
            "model": model,
            "oh_encoder": encoder,
            "lb": lb,
            "feature_names": train_data.drop(columns=[model_config["target_feature_name"]]).columns,
        }
        pickle.dump(model_arfitact, fp)
