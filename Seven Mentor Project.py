# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:30:07 2021

@author: acer
"""




# Project on Support Vector Machine
# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
data=pd.read_csv('C://Users/acer/Downloads//train.csv')
print(data)


#Cehck the rows & Columns
data.shape

#Access the begin data 
data.head()

# Access the end data
data.tail()

#Describe index
data.index

# Check contain all rows fill or not?
data.count()

#Check the Data-types & Sub Data types
data.info()

# Stastical / Arithamatic Calculation
data.describe()

# Check the null values 
data.isnull().sum()


# All data Splitting.
#Spitting the data into independent  variables.
x=data.iloc[:, : -1]
x

# Check the contain value in column label of 'Blue'.
x['blue'].value_counts()


# Check the contain value in column label of 'wifi'.
x['wifi'].value_counts()

x.info()


# Spitting the data into dependent variable.
y=data.iloc[:, -1 :]
y


# Check the contain value in column label of 'price_range'.
y['price_range'].value_counts()

y.info()

# Converting the integer data into Category data.
y['price_range']=y['price_range'].astype('category')
y['price_range'].head()




#Visualization the data with Co-relation.
sn.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()


sn.lineplot(x['battery_power'], x['blue'], color='lightblue')
plt.show()


sn.scatterplot(x['battery_power'], x['blue'], color='red')
plt.show()


sn.barplot(y['price_range'], x['battery_power'])
plt.show()



sn.boxplot(y['price_range'], x['battery_power'])
plt.show()



sn.violinplot(y['price_range'], x['battery_power'])
plt.show()



# Spitting the data Training & Testing process
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.10, random_state=7)
x_train.shape

y_train.shape


x_test.shape

y_test.shape


# Compare the independent variable training data & independent variable testing data respectively.

sn.pairplot(x_train)
plt.show()


sn.pairplot(x_test)
plt.show()


# Fitting the Algorithm of best accuarcy.
from sklearn.svm import SVC
rn=SVC(kernel='poly')   #rbf=94.5 & poly=96.5
model=rn.fit(x_train, y_train)
print(model)


# Predict the model
y_pred=model.predict(x_test)
print(y_pred)



# Calculate the Accuarcy , confusion matrix and  Classification_report
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, recall_score
print(accuracy_score(y_test, y_pred)*100)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

print(recall_score(y_test, y_pred, average='weighted')*100)


# Visualization independent & dependent variable data.
plt.plot(y_test, y_pred, color='red',lw=4, label='Accuracy_of_model')
plt.xlabel('Independent_Variables')
plt.ylabel('Price_Range')
plt.title('Info_of_Mobile')
plt.legend(loc='upper left', shadow=True)
plt.show()



# plot the graph on predict data.

plt.scatter(x_test['battery_power'], y_test, color='red', label='battery_power')

plt.scatter(x_test['blue'], y_test, color='black',lw=3, label='blue')

plt.scatter(x_test['clock_speed'], y_test, color='green',lw=3, label='clock_speed')

plt.scatter(x_test['dual_sim'], y_test, color='orange', label='dual_sim')

plt.scatter(x_test['fc'], y_test, color='lightblue', label='fc')

plt.scatter(x_test['four_g'], y_test, color='gray', label='four_g')

plt.scatter(x_test['int_memory'], y_test, color='pink', label='int_memory')

plt.scatter(x_test['m_dep'], y_test, color='maroon', label='m_dep')

plt.scatter(x_test['mobile_wt'], y_test, color='violet', label='mobile_wt')

plt.scatter(x_test['n_cores'], y_test, color='silver', label='n_cores')

plt.scatter(x_test['pc'], y_test, color='yellow', label='pc')

plt.scatter(x_test['px_height'], y_test, color='cyan',lw=3, label='px_height')

plt.scatter(x_test['px_width'], y_test, color='purple',lw=3, label='px_width')

plt.plot(x_train, model.predict(x_train), color='lightblue', alpha=0.4)

plt.xlabel('Independent_Variable')
plt.ylabel('Dependent_Varibale = price_range')
plt.title('Information_of_Mobile')
plt.legend(loc='lower right', shadow=True, ncol=2)
plt.show()









