from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_request():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello!"}


def test_post_request():
    request_data = {
        "age": 39,
        "workclass": "State-gov",
        "fnlgt": 77516,
        "education": "Bachelors",
        "education-num": 13,
        "marital-status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital-gain": 2174,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "United-States",
    }
    resp = client.post("/prediction/", json=request_data)
    assert resp.status_code == 200
    assert resp.json() == {'predictions': ['<=50K']}


def test_post_request_more50():
    request_data = {
        "age": 45,
        "workclass": "Private",
        "fnlgt": 88500,
        "education": "Some-college",
        "education-num": 10,
        "marital-status": "Married-civ-spouse",
        "occupation": "Machine-op-inspct",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 44,
        "native-country": "United-States",
    }
    resp = client.post("/prediction/", json=request_data)
    assert resp.status_code == 200
    assert resp.json() == {'predictions': ['<=50K']}


def test_post_request_less50():
    request_data = {'age': 66,
                    'workclass': 'Private',
                    'fnlgt': 113323,
                    'education': 'Bachelors',
                    'education-num': 13,
                    'marital-status': 'Married-civ-spouse',
                    'occupation': 'Prof-specialty',
                    'relationship': 'Husband',
                    'race': 'White',
                    'sex': 'Male',
                    'capital-gain': 20051,
                    'capital-loss': 0,
                    'hours-per-week': 40,
                    'native-country': 'United-States'}

    resp = client.post("/prediction/", json=request_data)
    assert resp.status_code == 200
    assert resp.json() == {'predictions': ['>50K']}
