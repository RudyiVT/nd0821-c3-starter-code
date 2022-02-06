import yaml
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from starter.ml.data import process_data
from starter.ml.model import inference

with open("model/model.pkl", 'rb') as fp:
    model_artifacts = pickle.load(fp)

with open("config.yml") as fp:
    model_config = yaml.load(fp, Loader=yaml.FullLoader)["modeling"]


class FeatureVector(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int = Field(alias="education-num")
    marital_status: str = Field(alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hours_per_week: int = Field(alias="hours-per-week")
    native_country: str = Field(alias="native-country")


app = FastAPI()


@app.get("/")
async def root_request():
    return {"message": "Hello!"}


@app.post("/prediction/")
async def run_inference(data: FeatureVector):
    X = pd.DataFrame(data.dict(), index=[0])
    X.columns = [x.replace("_", "-") for x in X.columns]
    X = X[model_artifacts.get("feature_names")]

    X_processed, _, _, _ = process_data(X,
                                        categorical_features=model_config["categorical_fature_names"],
                                        encoder=model_artifacts.get('oh_encoder'),
                                        training=False)
    encod_preds = inference(model_artifacts.get('model'), X_processed)
    predictions = model_artifacts.get('lb').inverse_transform(encod_preds)
    return {"predictions": list(predictions)}
