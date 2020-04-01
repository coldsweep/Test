# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:43:25 2020

@author: Soham Ghosh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle

customer_data = pd.read_csv(r'C:\Users\Soham Ghosh\OneDrive\Desktop\customer_churn - Copy (2).csv')
dataset = customer_data.drop(['CallMinutes', 'AgeGroup', 'Plan','PhoneType'], axis=1)
CallMinutes = pd.get_dummies(customer_data.CallMinutes).iloc[:,0:]
AgeGroup = pd.get_dummies(customer_data.AgeGroup).iloc[:,0:]
Plan = pd.get_dummies(customer_data.Plan).iloc[:,0:]
dataset = pd.concat([dataset,CallMinutes,AgeGroup,Plan], axis=1)
X =  dataset.drop(['Churn'], axis=1)
y = dataset['Churn']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=200, random_state=0)  
classifier.fit(X_train, y_train)  
predictions = classifier.predict(X_test)
from sklearn.metrics import classification_report, accuracy_score

pickle.dump(classifier, open('model.pkl','wb'),protocol=2)    