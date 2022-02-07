# Script to train machine learning model.
import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import pickle

from ml.data import process_data
from ml.model import train_model, compute_model_metrics, get_model_performance_on_slice

if __name__ == "__main__":
    # Load cleaned dataset
    data = pd.read_csv("../data/census_cleaned.csv")

    # Load configs for training pipeline
    with open("../config.yml") as fp:
        model_config = yaml.load(fp, Loader=yaml.FullLoader)["modeling"]

    # split dataset on train and test parts
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

    # preprocess testing dataset
    X_test, y_test, encoder, lb = process_data(
        X=test_data,
        categorical_features=model_config["categorical_fature_names"],
        label=model_config["target_feature_name"],
        encoder=encoder,
        lb=lb,
        training=False,
    )

    preds = model.predict(X_test)

    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")

    # save model and encoders
    with open("../model/model.pkl", 'wb') as fp:
        model_arfitact = {
            "model": model,
            "oh_encoder": encoder,
            "lb": lb,
            "feature_names": train_data.drop(columns=[model_config["target_feature_name"]]).columns,
        }
        pickle.dump(model_arfitact, fp)

    # train different models in slices
    with open("slice_output.txt", 'w+') as fp:
        for cat_column_name in model_config["categorical_fature_names"]:
            precision, recall, fbeta = get_model_performance_on_slice(data, slice_columns=[cat_column_name])
            fp.write(
                f"precision: {round(precision, 3)},"
                f"recall: {round(recall, 3)}, "
                f"fbeta: {round(fbeta, 3)} "
                f"for one feature {cat_column_name}"
            )
            fp.write("\n")
