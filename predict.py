import pandas as pd
import pickle
from collections import defaultdict
import numpy as np
from setting import WoECat, WoENom



#format output
# {
#     "model":"german-credit-risk",
#     "version": "1.0.0",
#     "score_proba":{result}
#
# }
# raw_input ={"person_home_ownership": "MORTGAGE",
#   "loan_intent": "DEBTCONSOLIDATION",
#   "loan_grade": "C",
#   "cb_person_default_on_file": "N",
#   "person_age": 29,
#   "person_income": 95000,
#   "person_emp_length": 4.0,
#   "loan_int_rate": 13.72,
#   "loan_percent_income": 0.03,
#   "cb_person_cred_hist_length": 9,
#   "loan_amnt": 2400}

features_list =["person_home_ownership",
  "loan_intent",
  "loan_grade",
  "cb_person_default_on_file",
  "person_age",
  "person_income",
  "person_emp_length",
  "loan_int_rate",
  "loan_percent_income",
  "cb_person_cred_hist_length",
  "loan_amnt"]
class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(__name__, name)
        except AttributeError:
            return super().find_class(module, name)

preprocess = CustomUnpickler(open("trained_model/FE-WOE-1.0.0.pkl", "rb")).load()

# with open("trained_model/FE-WOE-1.0.0.pkl", "rb") as f_in: #A
#     preprocess= pickle.load(f_in) #B
model = CustomUnpickler(open("trained_model/M-XGB-1.0.0.pkl", "rb")).load()


def formating_data(raw_input):
    # pandas dataframe
    # urutan colomn
    raw_input = pd.DataFrame.from_dict(raw_input, orient="index").T.replace({
        None: np.nan,
        "null":np.nan,
        "" : np.nan


    })
    features = features_list
    return raw_input[features]
def preprocess_data(raw_input):
    """
    acct dictionary format input
    return pandas / numpy with the same format as development
    """
    # validate data
    X = preprocess.transform(raw_input)
    return X


def predict_data(data):
    # load model
    # input dict
    # preprocess preprocess_data
    # return final predictions
    data = formating_data(data)
    data = preprocess_data(data)
    result = model.predict_proba(data)[:,1]
    return round(result[0],6)

# if __name__ == "__main__":
#     # print(y)
#
#     result = predict_data(raw_input)
#     # print(type(result))
#     print(result)
#     # assert score_proba == result
