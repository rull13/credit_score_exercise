from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class WoECat(BaseEstimator, TransformerMixin):
    def __init__(self, feature_name):
        self.feature_name = feature_name
    def fit(self, X, y = None):
        return self
    def transform(self, X, y = None):
        X_ = X.copy() # creating a copy to avoid changes to original dataset
        for i in self.feature_name:
            if i == 'person_home_ownership':
                X_[f'{i}_WOE'] = np.where(X_[i].isin(['MORTAGE']), -0.682,
                      np.where(X_[i].isin(['OTHER']), 0.468,
                      np.where(X_[i].isin(['OWN']), -1.24,
                     np.where(X_[i].isin(['RENT']), 0.502, 0))))
            elif i == 'loan_intent':
                X_[f'{i}_WOE'] = np.where(X_[i].isin(['DEBTCONSOLIDATION']), 0.360,
                  np.where(X_[i].isin(['EDUCATION']), -0.293,
                  np.where(X_[i].isin(['HOMEIMPROVEMENT']), 0.2355,
                 np.where(X_[i].isin(['MEDICAL']), 0.267,
                np.where(X_[i].isin(['PERSONAL']), -0.117,
                np.where(X_[i].isin(['VENTURE']), -0.472,0))))))
            elif i == 'loan_grade':
                X_[f'{i}_WOE'] = np.where(X_[i].isin(['A']), -0.925,
                  np.where(X_[i].isin(['B']), -0.361,
                  np.where(X_[i].isin(['C']), -0.064,
                 np.where(X_[i].isin(['D']), 1.64,
                np.where(X_[i].isin(['E']), 1.87,
                np.where(X_[i].isin(['F']), 2.14,
                         np.where(X_[i].isin(['G']), 5.41,0)))))))
            elif i == 'cb_person_default_on_file':
                X_[f'{i}_WOE'] = np.where(X_[i].isin(['N']), -0.213,
                  np.where(X_[i].isin(['Y']), -0.778, 0))
        X_ = X_.drop(self.feature_name, axis=1)
#         display(X_)
        return X_

class WoENom(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y = None):
        return self
    def transform(self, X, y = None):
        X_ = X.copy() # creating a copy to avoid changes to original dataset
        #do nothing
#         display(X_)
        return X_
