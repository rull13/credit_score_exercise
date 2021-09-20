## Heroku Deployment Access

[Credit_Risk_Exercise](https://credit-score-exercise.herokuapp.com/)

# Credit Risk Exercise

using `credit_risk_dataset.csv` file available under `notebooks/`

The dataset is composed by `32581` rows (observations) and `12` columns (variables).

- `person_age` : is the age of the person at the time of the loan.
- `person_income`: is the yearly income of the person at the time of the loan.
- `person_home_ownership`: is the type of ownership of the home.
- `person_emp_length`: is the amount of time in years that person is employed.
- `loan_intent`: is the aim of the loan.
- `loan_grade`: is a classification system that involves assigning a quality score to a loan based on a borrower's credit history, quality of the collateral, and the likelihood of repayment of the principal and interest.
- `loan_amnt`: is the dimension of the loan taken.
- `loan_int_rate`: is the interest paid for the loan.
- `loan_status`: is a dummy variable where 1 is default, 0 is not default.
- `loan_percent_income`: is the ratio between the loan taken and the annual income.
- `cb_person_default_on_file`: answers whether the person has defaulted before.
- `cb_person_cred_hist_length`: represents the number of years of personal history since the first loan taken from that person.

## How to Use

1. To use locally install all the requirements from file `requirements.txt`, using `pip install -r requirements.txt`
2. Run `app.py` to run python webserver and the application
3. Open `127.0.0.1:3000`

## Model Deployment

### Handling Missing Value
- There 2 feature that have a missing value `person_emp_length` contains 2.75% NaN and `loan_int_rate` contains 9.56% NaN
- We create a new feature `person_emp_length_nan` and	`loan_int_rate_nan` and fill nan values with median, the old feature that has nan values still exist in dataframe
- Model will try to use all the features that have Nan or not and compare each result

### Handling Outlier value
- The outlier will be handled by using Weight of Evidence (WOE)
- The old features and WOE features will be in the different models and the result will be compared.

### Model Evaluation

| Model || Train || Valid|| Holdout Sample|
| --- | --- | --- |--- | --- | --- | --- |
||Accuracy	|AUC	|Accuracy|	AUC|	Accuracy|	AUC|
|XGB OPT WOE CAT	|0.941270|	0.869816|	0.938476|	0.865756|	0.933045|	0.852295|
|XGB OPT DUMMY	|0.940257|	0.868141|	0.933076|	0.855592|	0.931348	|0.851468|
|RFR OPT WOE CAT|	0.914364	|0.813566	|0.914947	|0.814282|	0.913453|	0.809761|
|XGB OPT WOE	|0.892136	|0.780135|	0.875796|	0.749947|	0.886301|	0.767530|
|LogReg WOE OPT	|0.846280	|0.710719|	0.840694|	0.697469|	0.848504|	0.710803|
|RFR OPT WOE	|0.856743|	0.688594|	0.850723|	0.671920|	0.857143|	0.684250|
|LogReg OPT WOE CAT	|0.815902|	0.601540|	0.812343|	0.595295|	0.820734|	0.606344|

### Pipeline
- Using Model XGBoost and Weight of Evidence in categorical features
- Create a WOE in the pipeline for preprocessing
- Create an XGBmodel in pipeline to predict new data

## Guidance

### Example Input and Output Format
- This example if you want input data using `postman`
- This input need to be post under this endpoint:
`127.0.0.1:3000/pred` or `https://credit-score-exercise.herokuapp.com/pred`
- `Content-Type : application/json`
- This input using `POST` method, with arguments:

|Field|	Description|	Value|
| --- | --- | --- |
|person_age	|Age.	|Integer|
|person_income	|Annual Income.|	Integer|
|person_home_ownership	|Home ownership.	|'RENT', 'MORTGAGE', 'OWN', or 'OTHER'|
|person_emp_length|	Employment length (in years)	|Integer|
|loan_intent	|Loan intent.|	'PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', or 'DEBTCONSOLIDATION'|
|loan_grade|	Loan grade.|	'A', 'B', 'C, 'D', 'E', 'F', or 'G'|
|loan_amnt|	Loan amount.|	Integer|
|loan_int_rate|	Interest rate.	|Float|
|loan_percent_income	|Percent income.|	Float|
|cb_person_default_on_file	|Historical default.|	'Y', or 'N'|
|cb_person_cred_hist_length	|Credit history length.	|Integer|

```json
{"person_home_ownership": "MORTGAGE",
  "loan_intent": "DEBTCONSOLIDATION",
  "loan_grade": "C",
  "cb_person_default_on_file": "N",
  "person_age": 29,
  "person_income": 95000,
  "person_emp_length": 4.0,
  "loan_int_rate": 13.72,
  "loan_percent_income": 0.03,
  "cb_person_cred_hist_length": 9,
  "loan_amnt": 2400}
```
-  After sending the input through postman, python `app.py` will return predicted data

|Field|	Description|
| --- | --- |
|model	|The machine learning model.|
|score_proba	|Probability estimates.|
|version|	Model version.|

```json
{
        "model":"credit_risk_exercise",
        "score_proba":"0.059884",
        "version": "1.0.0"


    }
```
- HTTP Method using GET and POST from flask API
