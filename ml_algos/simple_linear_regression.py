# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:39:07 2021

@author: barsh
"""

#1 import some packages(numpy,pandas,sklearn,matplotlib)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2 Read the dataset

dataset = pd.read_csv('salary_data.csv')

#3 We need to split the data based on independent(x) and
# dependent(y) variables
 
x = dataset.iloc[:,:-1].values

y = dataset.iloc[:,1].values

#4. Divide the complete dataset into training and test dataset

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(x, y, test_size = 1/3, random_state = 0 )

#5. implement our regression stuff 

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

pred = lr.predict(X_test)


#implement the graph

sns.regplot(X_train, y_train, color = 'red')
#plt.plot(X_train,lr.predict(X_test))
#plt.show()
