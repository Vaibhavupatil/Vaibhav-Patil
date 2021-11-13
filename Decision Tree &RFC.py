# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:01:47 2021

@author: acer
"""

#  Decision Tree used for both Regression & classification. But mostly referred to classisfication.
# its consits of decision node & leaf node = branches is indicated the decision rule,  leaf node is represent the outcome & internal node  represent the features of dataset.
#Root Node: Root node is from where the decision tree starts. It represents the entire dataset, which further gets divided into two or more homogeneous sets.
#Leaf Node: Leaf nodes are the final output node, and the tree cannot be segregated further after getting a leaf node.
#Splitting: Splitting is the process of dividing the decision node/root node into sub-nodes according to the given conditions.

#Advantages of the Decision Tree
# It is simple to understand as it follows the same process which a human follow while making any decision in real-life.
# It can be very useful for solving decision-related problems.
# It helps to think about all the possible outcomes for a problem.
# There is less requirement of data cleaning compared to other algorithms.

# Disadvantages of the Decision Tree
# The decision tree contains lots of layers, which makes it complex.
# It may have an overfitting issue, which can be resolved using the Random Forest algorithm.
# For more class labels, the computational complexity of the decision tree may increase.


import pandas as pd
import numpy as np
#Height_Hair_Lenght_Vioce_pich
x=[[167,12,0], [135,30,1],[145,45,1],[176,10,0],[155,15,0]]

#class
y=['M', 'F','F', 'M', 'M']

from sklearn.tree import DecisionTreeClassifier

Classifier=DecisionTreeClassifier()

Classifier.fit(x,y)

y_pred=Classifier.predict([[123,23,1]])

print(y_pred)

print('Accuracy is:', Classifier.score(x,y)*100)



import pandas as pd
import numpy as np
dataset=pd.read_csv("banknotes.csv")
print(dataset)
dataset.head()
dataset.tail()
dataset.shape
dataset.info()
dataset.describe()

x=dataset.drop("Class", axis=1)   #axis 1 is consider a coloumn  while as 0 consider for rows.

y=dataset["Class"]


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.20, random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()

classifier.fit(x_train, y_train)

y_pred=classifier.predict(x_test)

df=pd.DataFrame({"actual":y_test, "pred":y_pred})

print(df)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

print("accuracy:", accuracy_score(y_test, y_pred)*100)




#-----------------------------------------------------------------------------------------------------------------------------






        
        
            #   Decision Tree Algorithm
            
            # Supervised ML ALgorithm
            
            # used for classification and regression problems.But mostly used in classification
            
            # Read the file
        
        

### Importing Libraries

import numpy as np
import pandas as pd

### 1. Read Dataset   ( 1 marks)

df=pd.read_csv('C://Users/acer/Downloads//adult_dataset.csv')
print(df)

### 2. Check top 5 and bottom 5 rows   ( 2 marks)

df.head()


df.tail()

### 3.a Check Size of data  ( 1 marks)

df.shape

### 3.b Check various datatypes in data  ( 1 marks)

df.info()

### 4. Check Statistical/ Mathmatical information  of data (1 marks)

df.describe()

### 5.Check missing values   ( 1 marks)

df.isnull().sum()

### 6. There are some ? that can been seen in data check it and get rid of it ( 5 marks)

#getting only the values of workclass is ? and assigning it to df1
df1=df[df['workclass']=='?']
df1.head()

#getting the data which doesnt have ?
df=df[df['workclass']!='?']
df.head()

# Lets see whether any other column contains '?',since '?' is a string,we can apply this check only on the ......
# .....categorical columns.

#select all categorical variables
df_categorical =df.select_dtypes(include=['object'])


#checking whether any other columns contain a '?'
df_categorical.apply(lambda x:x=='?',axis=0).sum()



# Thus the columns occupation and native.country contain some '?'s.Lets get rid of them.

#dropping the '?'s
df=df[df['occupation']!='?']
df=df[df['native.country']!='?']

 # Now we have a clean dataframe which is ready for model building.

df.shape

df.head()

df.info()



### Apply label encoding to the new clean dataframe (3 marks)

#encode categorical variables using label encoder
#select all categorical variables
df_categorical =df.select_dtypes(include=['object'])
df_categorical.head()


#apply label encoder to df_categorical

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df_categorical=df_categorical.apply(le.fit_transform)
df_categorical

#convert target variable income to categorical
df_categorical['income']=df_categorical['income'].astype('category')
df_categorical.info()

# Now all the categorical variables are suitabaly encoded.Lets build the model

###  Splitting the data into train and test (70/30) (5 marks)



#Putting feature variable to X
X=df_categorical.drop('income',axis=1)
print(X)

#Putting response variable to y
y=df_categorical['income']
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=99)

X_train.head()



### Build a descision tree classifier & also print the confusion matrix ( 5 marks)
#Import descision tree classifier from sk learn library
from sklearn.tree import DecisionTreeClassifier

#Fitting the decession tree with default hyperparameters,apart from 
#max_depth which is 5 so that we can plot and read the tree

dt_default=DecisionTreeClassifier(max_depth=5)

# Fiting on Train data
dt_default.fit(X_train,y_train)



#Making predictions
y_pred=dt_default.predict(X_test)
print(y_pred)

#lets check the model Evaluation metrics of our default model

#Importing classification report and confusion matrix from sklearn metrics

#Printing classification report
from sklearn. metrics  import classification_report, confusion_matrix, accuracy_score
print(classification_report(y_test,y_pred))

print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))









### 10. Use GridSearch to find the best params for Decision  tree Classifier (hint k-fold = 5)  (5 marks)   

20 * 10 * 4 * 5

#GridSearchCV to find optimal max_depth
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
#specify number of folds for k-fold CV
n_folds =5

#parameters to build model on
parameters={'max_depth':range(1,10), 'min_samples_split':range(1,8), 'ccp_alpha': [0,0.,1,0.2,0.3,0.4]}

#instantiate the model
dtree=DecisionTreeClassifier(criterion='gini',random_state =7)

#fit tree on the training data
tree=GridSearchCV(dtree,parameters,cv=n_folds,scoring='accuracy')
tree.fit(X_train,y_train)

#scores of GridSearch CV
scores=tree.cv_results_
pd.DataFrame(scores).head(20)

param=tree.best_params_
param

tree.best_score_



param=tree.best_params_
param

tree.best_score_


### Creating model on best parameters

#2: Instantiating the model
d_tree_model = DecisionTreeClassifier(criterion='gini',random_state =100,
                                     max_depth=10, min_samples_split=9)

#3 Fit on Train data

d_tree_model.fit(X_train,y_train)

# Predict on Test Data

d_tree_model.predict(X_test)

#Printing classification report
print(classification_report(y_test,d_tree_model.predict(X_test)))


                    
                    
                    #     GridSearchCV
        
        # GridSearch CV to find optimal max_depth
        # Specify the number of fold- for k-fold CV

from sklearn.model_selection import KFold
from sklearn.model_selection import  GridSearchCV

n_folds=5

parameters={'max_depth': range(1,10),'min_samples_split':range(1,8),'ccp_alpha':[0,0.1,0.3,0.55]}

# instantiate the model
dtee=DecisionTreeClassifier(criterion='gini', random_state=100)


# fitting the model
tree=GridSearchCV(dtee, parameters, cv=n_folds, scoring='accuracy')
tree.fit(X_train, y_train)


# score of GridSearch Cv

scores=tree.cv_results_
pd.DataFrame(scores).head()


param=tree.best_params_
param

tree.best_score_


# Creating the mode based on best params given by gridsearchcv

#dtree_new=DecisionTreeClassifier(criterion='gini', random_state=100, 'ccp_alpha'











import pandas as pd
import numpy as np
data=pd.read_csv('banknotes.csv')
print(data)



from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
model=data.apply(le.fit_transform)
print(model)


x=model.iloc[:, : -1]
print(x)

model['Class']=model['Class'].astype('category')
model.info()

model.head()

y=model.iloc[:, -1 :]
print(y)

from sklearn.model_selection import train_test_split
x_train,  x_test, y_train, y_test=train_test_split(x,y, test_size=0.20, random_state=0)

print(x_train.shape)

print(x_test.shape)

print(y_train.shape)

print(y_test.shape)

from sklearn.tree import DecisionTreeClassifier
dtee=DecisionTreeClassifier(max_depth=5)
dtc=dtee.fit(x_train,y_train)
print(dtc)



y_pred=dtc.predict(x_test)
print(y_pred)


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred)*100)



from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

n_folds=7

parameters={'max_depth':range(1,11), 'min_samples_split':range(1,21), 'ccp_alpha':[0,0.1,0.2,0.55]}


dtee=DecisionTreeClassifier(criterion='gini', random_state=7)

tree=GridSearchCV(dtee, parameters, cv=n_folds, scoring='accuracy')
tree.fit(x_train, y_train)

score=tree.cv_results_
pd.DataFrame(score).head()
    

param=tree.best_params_
param

a=tree.best_score_
print(a*100)






# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






    # Random Forest Classifier 
                

import pandas as pd
import numpy as np
data=pd.read_csv("wisc_bc_data.csv")      # brain cancer
print(data)


data .describe()


data.shape
data.head()
data.tail()
data.info()
data.describe()

x=data.drop(["id", "diagnosis"], axis=1)
print(x)
x.info()

y=data["diagnosis"]
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.20, random_state=0)

from sklearn.ensemble import RandomForestClassifier

classifier=RandomForestClassifier(n_estimators=200, random_state=0)

classifier.fit(x_train, y_train)

y_pred=classifier.predict(x_test)
print(y_pred)



df=pd.DataFrame({"actual":y_test, "pred":y_pred})

print(df)


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(y_test, y_pred)*100)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test,y_pred))








                
                #   Random Forest CLassifier

## Random Forest Regressor RFR =  regression
## Random Forest  Classifier (RFC) Algorithm
# supervised Algorithm
# Ensembled method
# used to avoid overfitting
#  When imbalanced dataset


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('C://Users/acer/Downloads//winequalityN.csv')
print(data)

data['type'].value_counts()


data['quality'].value_counts()

data.info()



data.isnull().sum()

# We are amking teo categories in ouput 
# 'Good quality' and 'Bad quality' = 1  and 0
# 'Good quality' =1 = 7 or more than 7
# 'Bad quality' =0 = less than 7


data['Goodquality']=[1  if x>=7 else 0 for x in  data['quality']]
data.head()

data['Goodquality'].value_counts()


data['type'].value_counts()


df=data[data['type']=='red']
df.head()
df.shape


    #df=data[data['type']=='white']
    #df.head()
    #df.shape

df.drop(['type','quality'],axis=1, inplace=True)
df.head()

df.info()

df.isnul().sum()

# nan values is removed from all dataset
# if you want to  put any values for nan value, you can use following code
#df['fixed acidity'].replace(to_replace=np.nan, value=7, inplace=True)

#df['volatile acidity'].replace(to_replace=np.nan, value=7, inplace=True)
df.dropna()

df.isnull().sum()

df['citric acid'].plot.hist(bins=12, alpha=0.4)

plt.hist(df['citric acid'])

df.corr()


### Seperate data into inpout and output

x=df.iloc[:, : -1]
print(x)

y=df.iloc[:, -1 :]
print(y)


x.head(2)

y.head(2)


from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
xx=sc.fit_transform(x)
print(xx)

xx=pd.DataFrame(xx)
xx.head()

xx=xx.rename(columns={0:'fixed acidity',1:'volatile acidity'})
count=0

lst=[]
for i in lst:
    x=xx.rename({count:1})
    count=count+1
print(x)

    

from sklearn.feature_selection import chi2, SelectKBest
pre_model=SelectKBest(chi2, k=8)
x_kbest=pre_model.fit_transform(x,y)

pre_model.get_support()

x_kbest=pd.DataFrame(x_kbest)
x_kbest



                                
                
                #   Random Forest CLassifier
                
                ## Random Forest Regressor RFR =  Regression
                ## Random Forest  Classifier (RFC) Algorithm
                # supervised Algorithm
                # Ensembled method
                # used to avoid overfitting
                #  When imbalanced dataset
                
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv('C://Users/acer/Downloads//winequalityN.csv')
data.head()

data['type'].value_counts()

data['quality'].value_counts()

data.info()

# check the missing values.
data.isnull().sum()




#we are making only two categories in output 
#ie. 'good quality ' or 'bad quality' in the form 1 and 0 resp.
#quality having 7 or more than is considered as 1 and remaing is considered as 0

data['Goodquality'] = [1 if x >= 7 else 0 for x in data['quality']]
data['Goodquality'].value_counts()


data['type'].value_counts()

# In dataframe 'df' We are only considering 'red' type of wine
df=data[data['type']=='red']
df['type'].value_counts()

# as we can see here data set is having few features which contain missing values or blank space
# so now we need find those missing values and deal with it
#either drop it or replace by some value
df.info()

df.drop('type',axis=1,inplace=True)

df.drop('quality',axis=1,inplace=True)
df.info()

df.dropna()
df.isnull().sum()


# nan values is removed from all dataset
# if you want to  put any values for nan value, you can use following code
#df['fixed acidity'].replace(to_replace=np.nan, value=7, inplace=True)

#df['volatile acidity'].replace(to_replace=np.nan, value=7, inplace=True)

print(df['fixed acidity'].mean())

df['fixed acidity'].plot.hist(bins=12, alpha=0.5)

df['fixed acidity'].replace(to_replace=np.nan,value=7,inplace=True)

df.isnull().sum()

df['volatile acidity'].plot.hist(bins=12, alpha=0.5)

df['citric acid'].plot.hist(bins=12, alpha=0.5)

df['sulphates'].plot.hist(bins=12, alpha=0.5)

df['pH'].plot.hist(bins=12, alpha=0.5)

df['volatile acidity'].replace(to_replace=np.nan,value=0.5,inplace=True)
df['citric acid'].replace(to_replace=np.nan,value=0.1,inplace=True)
df['sulphates'].replace(to_replace=np.nan,value=0.6,inplace=True)
df['pH'].replace(to_replace=np.nan,value=3.3,inplace=True)

df.info()

df.isnull().sum()

#Upto this we have handled the missing data

df.corr()

df.head()

### Seperate data into inpout and output
x=df.iloc[:,:-1]
x.head()
y=df.iloc[:,-1:]
y.head()


#### min max scaler = value willl be lie  betweeen o and 1
from sklearn.preprocessing  import MinMaxScaler
sc=MinMaxScaler()
x=sc.fit_transform(x)
x=pd.DataFrame(x)
x=x.rename(columns={0:'fixed acidity',1:'volatile acidity',2:'citric acid',3:'residual sugar',4:'chlorides',5:'free sulfur dioxide',6:'total sulfur dioxide',7:'density',8:'pH',9:'sulphates',10:'alcohol'})
x.head()

from sklearn.feature_selection import chi2,SelectKBest

pre_model=SelectKBest(chi2,k=8)
kbest=pre_model.fit_transform(x,y)

pre_model.get_support()

x_kbest=pd.DataFrame(kbest)
x_kbest.head()

from sklearn.model_selection import train_test_split as tts
xtrain,xtest,ytrain,ytest=tts(x_kbest,y,test_size=0.2,random_state=1)

from sklearn.ensemble import RandomForestClassifier
model1=RandomForestClassifier()

model1.fit(xtrain,ytrain)
ypred=model1.predict(xtest)
ypred

from sklearn.metrics import accuracy_score,precision_score,confusion_matrix,recall_score

print(accuracy_score(ytest,ypred))

precision_score(ytest,ypred)

confusion_matrix(ytest,ypred)

recall_score(ytest,ypred)









import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
data=pd.read_csv('C://Users/acer/Downloads//winequalityN.csv')
print(data)


data.info()

data['type'].value_counts()

data['quality'].value_counts()


data.isnull().sum()


data['Goodquality']=[1 if x >=7 else 0 for x in data['quality']]

data['Goodquality'].value_counts()


df=data[data['type']=='red']
df



df.dropna()

df.isnull().sum()

df['fixed acidity'].plot.hist(bins=12, alpha=0.4, color='red')
df['fixed acidity'].replace(to_replace=np.nan, value=7, inplace=True)



df['volatile acidity'].plot.hist(bins=12, alpha=0.4, )
df['volatile acidity'].replace(to_replace=np.nan, value=7, inplace=True)



df['citric acid'].plot.hist(bins=12, alpha=0.4, color='yellow')
df['citric acid'].replace(to_replace=np.nan, value=7, inplace=True)


df['sulphates'].plot.hist(bins=12, alpha=0.4, color='green')
df['sulphates'].replace(to_replace=np.nan, value=7, inplace=True)


df['pH'].plot.hist(bins=12, alpha=0.4, color='black')
df['pH'].replace(to_replace=np.nan, value=7, inplace=True)

df.isnull().sum()

df.head()

df.info()

x=df.iloc[:, 1 : -2]
print(x.head())

x.info()

y=df.iloc[:, -1 :]

print(y)
y.info()

from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
model=sc.fit_transform(x)
print(model)

gg=pd.DataFrame(model)

gg.rename(columns={0:'fixed acidity', 1:'volatile acidity' ,2:'citric acid', 3:'residual sugar'})


lst=[]
count=0
for i in lst:
    x=gg.rename(columns={count:1})
    count=count+1
print(x)

x.info()
    
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.20, random_state=2)
print(x_train.shape)


print(x_test.shape)

print(y_train.shape)

print(y_test.shape)


from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier()
sor=forest.fit(x_train, y_train)
print(sor)


y_pred=sor.predict(x_test)
print(y_pred)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(y_test, y_pred)*100)

print(classification_report(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))












import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

data=pd.read_csv('C://Users/acer/Downloads//winequalityN.csv')
print(data)


data.info()

data.head()

data.isnull().sum()

df=data[data['type']=='red']
df

df.info()

df.isnull().sum()

df=df.drop('type', axis=1, inplace=True)

df=df.drop('quality', axis=1, inplace=True)


df.isnull().sum()

df['fixed acidity'].replace(to_replace=np.nan, value=7, inplace=True)
df['fixed acidity'].plot.hist(bins=12, alpha=0.8, color='red')


df['volatile acidity'].replace(to_replace=np.nan, value=7, inplace=True)
df['volatile acidity'].plot.hist(bins=12, alpha=0.8, color='cyan')


df['citric acid'].replace(to_replace=np.nan, value=7, inplace=True)
df['citric acid'].plot.hist(bins=12, alpha=0.8, color='green')


df['pH'].replace(to_replace=np.nan, value=7, inplace=True)
df['pH'].plot.hist(bins=12, alpha=0.8, color='yellow')


df['sulphates'].replace(to_replace=np.nan, value=7, inplace=True)
df['sulphates'].plot.hist(bins=12, alpha=0.8, color='pink')

df.head()

df.info()

x=df.iloc[:, 1 : -1]
print(x.head())

x.info()

y=df.iloc[:, -1 :]
print(y)

y.info()

from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
model=sc.fit_transform(x)
print(model)

ffg=pd.DataFrame(model)
print(ffg)

pd=ffg.rename(columns={0: 'fixed acidity',1 : 'volatile acidity'})

lst=[]
count=0
for i in lst:
    x=ffg.rename(columns={count:1})
    count=count+1
print(x)

x.info()

from sklearn.feature_selection import chi2, SelectKBest
dff=SelectKBest(chi2, k=7)
llp=dff.fit_transform(x,y)
print(llp)

dff.get_support()



from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(llp,y,test_size=0.20, random_state=5)

print(x_train.shape)

print(x_test.shape)

print(y_train.shape)

print(y_test.shape)


from sklearn.ensemble import RandomForestClassifier
scot=RandomForestClassifier()
lol=scot.fit(x_train, y_train)
print(lol)

y_pred=lol.predict(x_test)
print(y_pred)


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(y_test, y_pred)*100)

print(classification_report(y_test,y_pred))

print(confusion_matrix(y_test, y_pred))





import pandas as pd
import numpy as np
data=pd.read_csv('C://Users/acer/Downloads//petrol_consume.csv')
print(data)


data.head()

data.info()


x=data.iloc[:, : -1]
print(x)

x.head()


y=data.iloc[:, -1 :]
print(y)

y.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.20, random_state=5)
print(x_train)

print(y_test.shape)

print(x_test.shape)

from sklearn.ensemble import RandomForestClassifier
forst=RandomForestClassifier()
model=forst.fit(x_train, y_train)
print(model)

y_pred=model.predict(x_test)
print(y_pred)


from sklearn.metrics  import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(y_test, y_pred)*100)

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))








import pandas as pd
import numpy as np
data=pd.read_csv('wisc_bc_data.csv')
print(data)

data.head()


xx=data.drop('id', axis=1, inplace=True)
print(xx)

x=data.iloc[:, 1 : ]
print(x)


y=data.iloc[:, 0:1]
print(y)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.20, random_state=5)

print(x_train.shape)

print(x_test.shape)

print(y_test.shape)


print(y_train.shape) 
               

from sklearn.tree import DecisionTreeClassifier
dtee=DecisionTreeClassifier()
model=dtee.fit(x_train, y_train)
print(model)


y_pred=model.predict(x_test)
print(y_pred)


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(y_test, y_pred)*100)

print(classification_report(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))


from sklearn.model_selection  import KFold
from sklearn.model_selection import GridSearchCV

n_folds=5

parameters={'max_depth':range(1,21), 'min_samples_split':range(1,12), 'ccp_alpha':[0,0.1,0.4,0.55]}


dtee=DecisionTreeClassifier(criterion='gini', random_state=7)

tree=GridSearchCV(dtee, parameters, cv=n_folds, scoring='accuracy')
tree.fit(x_train, y_train)



model=tree.cv_results_
pd.DataFrame(model)

param=tree.best_params_
param

tree.best_score_*100





import pandas as pd
import numpy as np
data=pd.read_csv('letterdata.csv')
print(data)

data.head()

data.info()


x=data.iloc[:, 1 : -1]
print(x)

y=data.iloc[:, 0 : 1]
print(y)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.20, random_state=5)

print(x_train)

print(x_test.shape)

print(y_train.shape)

print(y_test.shape)


from sklearn.tree import DecisionTreeClassifier
dtee=DecisionTreeClassifier(max_depth=7)
tree=dtee.fit(x_train, y_train)
print(tree)


y_pred=tree.predict(x_test)
print(y_pred)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred)*100)

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test, y_pred))


print(classification_report(y_test, y_pred))




from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

parameters={'max_depth':range(1, 10), 'min_samples_split':range(1,11), 'ccp_alpha':[0,0.55,0.22,0.8]}

tree=DecisionTreeClassifier(criterion='gini', random_state=99)

dtee=GridSearchCV(tree, parameters, cv=2, scoring='accuracy')
dtee.fit(x_train, y_train)


core=dtee.cv_results_
pd.DataFrame(core)

param=dtee.best_params_
param


dtee.best_score_*100









import pandas as pd
import numpy as np
data=pd.read_csv('C://Users/acer/Downloads//adult_dataset.csv')
print(data)

data.head()

data.isnull().sum()


x=data.iloc[:, : -1]

y=data.iloc[ : ,-1 :]
y.head()

y.info()

y['income']=y['income'].astype('category')
y['income'].head()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
vcb=x.apply(le.fit_transform)
print(vcb)

vcb.head()

vcb.info()

data['age'].value_counts()


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(vcb, y, test_size=0.20, random_state=11)

print(x_train)

print(x_test.shape)

print(y_train.shape)

print(y_test.shape)

from sklearn.tree import DecisionTreeClassifier
cor=DecisionTreeClassifier(max_depth=2)
aor=cor.fit(x_train, y_train)
print(aor)


y_pred=aor.predict(x_test)
print(y_pred)


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(y_test, y_pred)*100)

print(classification_report(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))




from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

parameters={'max_depth':range(1,8), 'min_samples_split':range(1,9), 'ccp_alpha':[0,0.22,0.33]}

dtee=DecisionTreeClassifier(criterion='gini', random_state=7)

tree=GridSearchCV(dtee, parameters, cv=4, scoring='accuracy')
tree.fit(x_train, y_train)


mpj=tree.cv_results_
pd.DataFrame(mpj)

param=tree.best_params_
param

tree.best_score_*100



