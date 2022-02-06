# Instructions

[Github project repo](https://github.com/RudyiVT/nd0821-c3-starter-code)

[Live API endpoint](https://census-prediction-api.herokuapp.com)

## S3
To push data `dvc push -r s3-remote`, to pull `dvc pull -r s3-remote`

## Heroku deployment
create heroku app `heroku create census-prediction-api --buildpack heroku/python`

command to set aws creds to heroku `heroku config:set AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... --app app_name`

buildpacks `heroku buildpacks --app census-prediction-api`

`heroku git:remote -a census-prediction-api`

push heroku `git push heroku master`

open cli on heroku `heroku run bash --app census-prediction-api`


## Query live API
Live API [docs](https://census-prediction-api.herokuapp.com/docs)

Examples of live API testing provided in `/census/starter/leve_api_testing.ipynb`