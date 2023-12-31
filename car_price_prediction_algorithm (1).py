# -*- coding: utf-8 -*-
"""Car_price_prediction_algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SUl-AqNMApzU0M4rWa1yun0yrnEene87

Step 1: Importing the necessary libraries

Code Segment 1:
"""

import warnings
warnings.filterwarnings('ignore')

#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Code Segment 2:"""

from google.colab import drive
drive.mount('/content/drive')

"""Code Segment 3:"""

cars = pd.read_csv('/content/drive/MyDrive/prices.csv')

"""Code Segment 4:"""

cars.head()

"""Code Segment 5:"""

# Defining the map function
def dummies(x,df):
    temp = pd.get_dummies(df[x], drop_first = True)
    df = pd.concat([df, temp], axis = 1)
    df.drop([x], axis = 1, inplace = True)
    return df
# Applying the function to the cars_lr


cars = dummies('State',cars)
cars = dummies('Make',cars)
cars = dummies('Model',cars)

cars.head()

"""Code Segment 6:"""

from sklearn.model_selection import train_test_split

np.random.seed(0)
df_train, df_test = train_test_split(cars, train_size = 0.7, test_size = 0.3, random_state = 100)

"""Code Segment 7:*italicized text*"""

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
num_vars = ['Mileage']
df_train[num_vars] = scaler.fit_transform(df_train[num_vars])

df_train.head()

"""Code Segment 8:"""

#Dividing data into X and y variables
y_train = df_train.pop('Price')
X_train = df_train

import pandas as pd

# Assuming 'X_train' contains both numeric and categorical columns
# Use pd.get_dummies to one-hot encode categorical columns
X_train_encoded = pd.get_dummies(X_train)

# Now, 'X_train_encoded' should contain only numeric values

"""Code Segment 9:"""

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

"""Code Segment 10:"""

lm = LinearRegression()
lm.fit(X_train,y_train)

"""Code segment 11:"""

def build_model(X,y):
    X = sm.add_constant(X) #Adding the constant
    lm = sm.OLS(y,X).fit() # fitting the model
    print(lm.summary()) # model summary
    return X

"""Code segment 12:"""

X_train_new = build_model(X_train,y_train)

"""code segment 13:"""

scaler = MinMaxScaler()
num_vars = ['Mileage']
df_test[num_vars] = scaler.fit_transform(df_test[num_vars])

y_test = df_test.pop('Price')
X_test = df_test

"""Code segment 14:"""

# Making predictions
y_pred = lm.predict(X_test)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)