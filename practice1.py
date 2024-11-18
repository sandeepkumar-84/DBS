
"""
                                Module Title:	Machine Learning and Pattern Recognition
                                Module Code:	B9DA109
                                Module Leader:	Mark Germaine
                                Assessment Title:	Supervised Machine Learning – (Regression/Classification)
                                **Group Members**
                                Nitish
                                Sandeep Kumar
                                Vrinda 
                                Yash Kamdar
"""

# Importing all necessary libraries.  

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import tree
from pydotplus import graph_from_dot_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, auc, precision_recall_curve, confusion_matrix
#from sklearn.metrics import plot_confusion_matrix, plot_precision_recall_curve
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

################################ 2. Data Description #################################################
# Reading the dataset 
# The file can be kept at the local at C:\AssignmentFiles\CreditCardDefaultDataSet.csv to be read from 
# Another option is to use the online link of the github where this dataset csv file is located.  

dsCreditCardDefault = pd.read_csv('C:\AssignmentFiles\CreditCardDefaultDataSet.csv', index_col='ID')

#dsCreditCardDefault = pd.read_csv('https://raw.githubusercontent.com/sandeepkumar-84/DBS/refs/heads/asm_ca_01_ml/CreditCardDefaultDataSet.csv', index_col='ID')


# The current dataset looks like 

print("Before Data Cleaning dataset looks like ")
pd.set_option('display.max_columns', None)
print(dsCreditCardDefault.head())

################################ 2. Data Visualization #################################################
################################ End of Data Visualization #################################################

################################ 3. Data Prepararion #################################################
# 2.a Renaming of the columns since there are inconsistencies like the sequence used in columns, spaces in the column names and 
#       lower casing is used. PAY_0 Columns headers needs to be corrected as it should have been started from index 1 instead of 0. 

dsCreditCardDefault.rename(columns={'PAY_0': 'PAY_1'}, inplace=True)

#       column "default payment next month" name is changed to DEFAULT

dsCreditCardDefault.rename(columns={'default payment next month':'DEFAULT'}, inplace=True)

print("Checking the dataset info")
print(dsCreditCardDefault.info())

# From output it is evident that there are no null values present in any of the columns as all the columns have 30000 count. 
# Education categories which are not valid, and are still listed in the dataset are removed. 
# a.	1 = graduate school; 2 = university; 3 = high school; 4 = others,  are valid values. 
# Dataset has categories from 0 till 6. Therefore, entries with education categories values of 0, 5,6 are required to be deleted. 


print(f"Before deleting rows the Data Set Size is :\t{dsCreditCardDefault.shape[0]}")

def deleteRows(ddsCreditCardDefault, colName, value):
    ddsCreditCardDefault1 = ddsCreditCardDefault.drop(ddsCreditCardDefault[ddsCreditCardDefault[colName] == value].index)
    return ddsCreditCardDefault1

    
dsCreditCardDefault = deleteRows(deleteRows(deleteRows(dsCreditCardDefault,'EDUCATION',6),'EDUCATION',5),'EDUCATION',0)

#2.	MARRIAGE categories which are not valid,  and are still listed in the dataset are removed.
#   Valid categories are 1-Married,2-Single,3-Others 
#   Dataset has 0 which is undefined so the rows with Marriage =0 deleted. 

dsCreditCardDefault = deleteRows(dsCreditCardDefault,'MARRIAGE',0)

print(f"After deleting rows the Data Set Size is :\t{dsCreditCardDefault.shape[0]}")

#3.	Pay_n has some invalid entries which are corrected by adding 1. 
#	Valid range is 	-1,0,1,2,3,4,5,6,7,8,9
#	Existing range is -2,-2,-0,1,2,3,4,5,6,7,8. This can be corrected by adding 1. 

print(f"Before payment column is corrected")
print(dsCreditCardDefault[['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']].describe())

def correctPayColumn(df, paycol):
    df.loc[df[paycol]<0, paycol] = -1
    df.loc[df[p]>=0, p] = df.loc[df[p]>=0, p] + 1
    df[p] = df[p].astype('int64')
    return df

payCols = ['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']
for p in payCols:
    correctPayColumn(dsCreditCardDefault,p)

print(f"After payment column is corrected")
print(dsCreditCardDefault[['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']].describe())

# 4 Handling Categorical Features

#Application of One-hot encoding technique for representing categorical data (EDUCATION, SEX, and MARRIAGE) as numerical vectors. 
# The columns MALE Sex and Education columns are dropped and replaced with corresponding Boolean type columns representing if an 
# individual is male or not, if he is graduated or not, if he is at UNIVERSITY\HIGH_SCHOOL level or not and if he is married or not. 

dsCreditCardDefault['MARRIED'] = (dsCreditCardDefault['MARRIAGE'] == 1).astype('category')
dsCreditCardDefault.drop('MARRIAGE', axis=1, inplace=True)
dsCreditCardDefault['MALE'] = (dsCreditCardDefault['SEX'] == 1).astype('category')
dsCreditCardDefault.drop('SEX', axis=1, inplace=True)
dsCreditCardDefault['GRAD_SCHOOL'] = (dsCreditCardDefault['EDUCATION'] == 1).astype('category')
dsCreditCardDefault['UNIVERSITY'] = (dsCreditCardDefault['EDUCATION'] == 2).astype('category')
dsCreditCardDefault['HIGH_SCHOOL'] = (dsCreditCardDefault['EDUCATION'] == 3).astype('category')
dsCreditCardDefault.drop('EDUCATION', axis=1, inplace=True)

print(dsCreditCardDefault.head())


################################ End of Data Prepararion #################################################
################################ 4. Model Development and Evaluation ################################ #####

#Splitting into Features and Target

#Next, split your data into X (the features we will use to predict the target) and y (the target variable we want to predict). 
#In this example, the target variable is 'DEFAULT'

y = dsCreditCardDefault['DEFAULT']
X = dsCreditCardDefault.drop('DEFAULT', axis=1, inplace=False)

#Splitting into Training and Test sets

#Finally, use train_test_split from sklearn.model_selection to divide data into training and test sets. 
# This step is important to check model performance.

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=24, stratify=y)

display_training = {
    "Training":[np.shape(X_train)[0],len(y_train[y_train==1]),len(y_train[y_train==0])],
    }

display_test= {    
    "Test":[np.shape(X_test)[0],len(y_test[y_test==1]),len(y_test[y_test==0])],
}

tr_df = pd.DataFrame(data=display_training, index=["Shape","Defaulters","Non-defaulters"])
ts_df = pd.DataFrame(data=display_test, index=["Shape","Defaulters","Non-defaulters"])

print('\n',tr_df)
print('\n',ts_df)


# Plotting the data
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)


axes[0].bar(display_training.keys(), display_training.values(), color=['salmon', 'skyblue'])

axes[0].set_title('Training Set (Shape: np.shape(X_train)[0])')
axes[0].set_ylabel('Count')
axes[0].set_ylim(0, 20000)


axes[1].bar(display_test.keys(), display_test.values(), color=['salmon', 'skyblue'])
axes[1].set_title('Test Set (Shape: np.shape(X_test)[0])')
axes[1].set_ylim(0, 20000)

# Main title
plt.suptitle('Distribution of Defaulters and Non-defaulters in Training and Test Sets')

# Display the plot
plt.show()