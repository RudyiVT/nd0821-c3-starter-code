import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import yaml


def get_inference_pipeline(numeric_feature_names: list, categorical_feature_names: list) -> Pipeline:
    """
    Pipeline generation for model inference.

    :param numeric_feature_names: list of numerical feature names
    :param categorical_feature_names: list of categorical feature names
    :return: inference pipeline
    """

    # define transformation for different feature types
    numeric_transformer = make_pipeline(SimpleImputer(), StandardScaler())
    categorical_transformer = make_pipeline(OneHotEncoder())

    # Set splitted transformation process
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, numeric_feature_names),
            ("categorical", categorical_transformer, categorical_feature_names),
        ],
        remainder="drop",
    )

    # Combine preprocessing and modeling in one pipeline
    pipe = Pipeline(
        steps=[("preprocessor", preprocessor), ("random_forest", RandomForestClassifier()), ]
    )

    return pipe


if __name__ == "__main__":
    with open("../config.yml") as fp:
        model_config = yaml.load(fp, Loader=yaml.FullLoader)["modeling"]

    data = pd.read_csv("../data/census_cleaned.csv.csv")

    Y = data.pop(model_config["target_feature_name"])
    X = data

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=model_config["test_size"])

    pipe = get_inference_pipeline(model_config["numerical_feature_names"], model_config["categorical_fature_names"])

    pipe.fit(X_train, Y_train)

    pipe.predict_proba(X_test)
