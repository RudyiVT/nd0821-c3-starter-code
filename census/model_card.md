# Model Card


## Model Details
Model and deploying modified developend by [Volodymyr Rudyi](rudyiv@gmail.com) from a [fork](https://github.com/udacity/nd0821-c3-starter-code) \
Model Date: 06.02.2022\
Model Version: 1.0.0\
Model Type: RandomForestClassifier


# Dataset
Extraction was done by Barry Becker from the 1994 Census database. A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)) 

Prediction task is to determine whether a person makes over 50K a year.
Attribute Information:


Targets variable : `salary` (>50K, <=50K)

|**Variable name**   |**type**    |**Possible values**   |
|----------------|--------|--------------|
|age|continuous||
|workclass| categorical| Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.|
|fnlwgt| continuous|
|education| categorical| Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.|
|education-num| continuous.|
|marital-status| categorical| Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.|
|occupation| categorical| Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.|
|relationship| categorical| Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.|
|race| categorical| White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.|
|sex| categorical| Female, Male.|
|capital-gain| continuous|
|capital-loss| continuous|
|hours-per-week| continuous|
|native-country| categorical| United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.|



More datailed infomation abount dataset could be found [here](https://archive.ics.uci.edu/ml/datasets/census+income)

## Intended Use
Model is a binary classification to predict if salary lower or higher then 50K 
Raw dataset contains whitespaces, it was cleaned manualy
Raw and cleanned dataset versioned via DVC using S3.
Model with required artifacts (One hot encoder, Label binarizer) also versioned via DVC.

## Training Data
Dataset randomly splitted on train and evaluation datasets (80%/20%). This ratio could be configures throught config file

## Evaluation Data
Random 20% of whole dataset

## Metrics
Model performence metrics on evaluation dataset:
precision: 0.7e, recall: 0.62, fbeta: 0.67


## Caveats and Recommendations
* Implement cross validation during traning proces
* Log experiments 
* Split ML steps and generate reproducible pipeline (all training steps should be combined into Pipe object)
* Feature generation and feature selection
* Test another algorithms not just Random Forest
* Deep analysis of model performence on slices.