from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd
from pygam import LinearGAM, s, f

class pygam(BaseEstimator):
    
    def __init__(self):
        self.my_pygam=LinearGAM(s(0) + s(1) + f(2))
        
    def fit(self, X, y):
        self.my_pygam.fit(X,y)

    def predict(self, X):
        return self.my_pygam.predict(X)