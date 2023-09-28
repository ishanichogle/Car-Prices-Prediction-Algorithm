# Car-Prices-Prediction-Algorithm
Link to the Google colab notebook: https://colab.research.google.com/drive/1SUl-AqNMApzU0M4rWa1yun0yrnEene87#scrollTo=nNlWLfjN5X0S
Following is the step by step explanation of the code written for price prediction:

Code segment 1: I downloaded the following libraries in order to run my code:

Numpy:
Pandas:
Matplotlib: 
Seaborn:

Code Segment 2: Uploaded the prices csv file to drive under the name prices.csv and allowed Google colab to access the file 

Code Segment 3: Read the prices,csv file into a dataframe . 

Code Segment 4: Get the titles of the main columns in the prices.csv file 

Since there are only six parameters, we will not be assessing them to remove unwanted ones which have o significant effect on the price prediction. 

Code segment 5: We convert the non numery factors into a boolean output so that we can apply linear regression on it. So since state, make and model were not really numeric values, we added extra columns and converted them into outputs of 0,1 values. 

Code Segment 6: Split the data in such a way that 70% of it will be used to train the regression model and 30% will be used for testing. Currently, have taken a random state value of 100. 

Code segment 7: Applied feature scaling on mileage factor since it had a wide range of values 

Code Segment 8: Declared the X and Y variables. 

Code segment 9: DOwnloaded the following:
LinearRegression

StatsModels,api

Variation_inflation_factor

The variance inflation factor (VIF) is a measure of how much the variance of a feature is inflated due to multicollinearity with other features. Multicollinearity is a problem that occurs when two or more features are highly correlated with each other. Multicollinearity can make it difficult to interpret the results of a linear regression model, and it can also lead to overfitting.

Code segment 10: We apply linear regression to the data 

Code segment 11 and 12: we build a model which will take inputs as our training sets 

Code segment 13: Now we move to test sets. We so scaling in this code and define X_test and y_test data sets. 

Code segment 14: we calculate how much efficient our current code is. As of now, the model is able to account for 39% of the variances in predicted and actual data. 


























