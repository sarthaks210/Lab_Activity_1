#buidling ML Model for breast cancer data
#importing the libraries
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Sarthak/Downloads/Cancer.csv")

df.head()

from sklearn linear. nodel import LogisticRegression
from sklearn. metrics import mean_squared_error
from sklearn-nodel. selection import train_test_split
import matelotlib-pyplot as plt

#Split the data into 80% training and 20% testing
*train, x_test, y_train, y_test - train test_split (x, y, test_size - 0.20)

#Create the models
#Create the 1inear regression model
1g - LogisticRegression(). fit (%_train, y_train)