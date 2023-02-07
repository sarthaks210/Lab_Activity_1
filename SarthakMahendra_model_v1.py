#buidling ML Model for breast cancer data
#importing the libraries
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Sarthak/Downloads/Cancer.csv")

df.head()

df = df.dropna()

df.shape

x = df.iloc[:,:10].values
y = df.iloc[:,10:].values

x

y


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

#Create the models
#Create the 1inear regression model
lg = LogisticRegression().fit(x_train, y_train)

#Show the model linear regression prediction
lg_prediction = lg.predict(x_test)
print(lg_prediction)


mse = mean_squared_error(lg_prediction,y_test)

rmse = math.sqrt(mse)

print(rmse)