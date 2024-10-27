# -*- coding: utf-8 -*-
"""Exercise_5_Pandas_Joining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ikf6wATZ7kmxWEg5-yLzZai2_NlG7GNg

Module Code: B9DA108 | Module Title: Programming for Data Analysis | School: DBS

Lecturer Name: Alexander Victor

Exercise 5: Pandas Merge and Plotting to be completed by date: Wednesday, 30 October 2024, 11:54 PM

Student Name: Sandeep Kumar | Student ID: 20049275 | Email: 20049275@mydbs.ie | Git: https://github.com/sandeepkumar-84/DBS.git

1) Write a Pandas program to append a list of dictioneries or series to an
existing DataFrame and display the combined data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stockPriceData = pd.read_csv("alphabet_stock_data.csv")

#Existing dataframe
std_data = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
        'marks': [200, 210, 190, 222, 199]}
std_df = pd.DataFrame(std_data)

print("Existing dataframe")
print(std_df)

# new dictionary
new_std = {'student_id':'S6', 'name':'Scarlette Fisher', 'marks':205}

# adding it in existing dataframe
std_df1 =  std_df._append(new_std, ignore_index=True)

print("After adding a new dictionary in the existing dataframe")
print(std_df1)
#

"""2) Write a Pandas program to join the two given dataframes a long rows and merge with another dataframe along the common column id."""

#
#student_data1:

data1={
        "student_id": ["S1", "S2", "S3", "S4", "S5"],
        "name": ["Danniella Fenton", "Ryder Storey", "Bryce Jensen", "Ed Bernal", "Kwame Morin"],
        "marks": [200, 210, 190, 222, 199]
}
df1=pd.DataFrame(data1)
print(df1)

#student_data2:
data2 = {
        "student_id": ["S4", "S5", "S6", "S7", "S8"],
        "name": ["Scarlette Fisher", "Carla Williamson", "Dante Morse", "Kaiser William", "Madeeha Preston"],
        "marks": [201, 200, 198, 219, 201]
}
df2=pd.DataFrame(data2)
print(df2)

#exam_data:

data3 = {
        "student_id": ["S1", "S2","S3", "S4", "S5", "S7","S8","S9","S10","S11","S12","S13"],
        "exam_id": [23, 45, 12, 67, 21,55,33,14,56,83,88,12]
        }
df3=pd.DataFrame(data3)
print(df3)

# join the two given dataframes a long rows

dfJOin1_2=pd.concat([df1,df2])
print(dfJOin1_2)

# Merge dfJOin1_2 with df3 along common column (student_id)

dfMerge3=pd.merge(dfJOin1_2,df3,on='student_id')
print(dfMerge3)

"""3. Write a Pandas program to join the two dataframes using the common column of both dataframes."""

#Write a Pandas program to join the two dataframes using the common column of both dataframes.
#student_data11:

data1 = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
         'marks': [200, 210, 190, 222, 199]}
dfStudent1 =  pd.DataFrame(data1)
print(dfStudent1)
#student_data2:
data2 = {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
         'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
         'marks': [201, 200, 198, 219, 201]}
dfStudent2 = pd.DataFrame(data2)
print(dfStudent2)
#Join the two dataframes using the common column of both dataframes.
#Common key of both the dataframe is student id. therefore considering it as common.
dfJoin=pd.merge(dfStudent1,dfStudent2,on='student_id')
print("Result")
print(dfJoin)

"""4. Write a Pandas program to join the two dataframes with matching
records from both sides where available
"""

#student_data11:

data1 = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
         'marks': [200, 210, 190, 222, 199]}
dfStudent1 =  pd.DataFrame(data1)
print(dfStudent1)
#student_data2:
data2 = {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
         'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
         'marks': [201, 200, 198, 219, 201]}
dfStudent2 = pd.DataFrame(data2)
print(dfStudent2)

#join the two dataframes with matching records from both sides where available
# using inner join to find out the matching records from both sides.
# only common key (i.e. student_id)  present in both the frames are displayed in this case.It
# is like inner join of sql

dfJoin=pd.merge(dfStudent1,dfStudent2,on='student_id',how='inner')
print(dfJoin)

"""4) Write a Pandas program to join (left join) the two dataframes using keys from left dataframe only."""

# using outer join to display all the entries from data1 and if the corresponding mathcing entry is present in
# data2 it will be displayed as y otherwsie NAN will be displayed in y. Its like left outer join of sql
#data1:
data1 = {'key1': ['K0', 'K0', 'K1', 'K2'],
         'key2': ['K0', 'K1', 'K0', 'K1'],
         'P': ['P0', 'P''1', 'P2', 'P3'],
         'Q': ['Q0', 'Q1', 'Q''2', 'Q3']}
df1 =  pd.DataFrame(data1)
print(df1)

#data2:
data2 = {'key1': ['K0', 'K1', 'K1', 'K2'],
         'key2': ['K0', 'K0', 'K0', 'K0'],
         'R': ['R0', 'R''1', 'R2', 'R3'],
         'S': ['S0', 'S1', 'S''2', 'S3']}
df2 = pd.DataFrame(data2)
print(df2)

#join (left join) the two dataframes using keys from left dataframe only.
dfJoin=pd.merge(df1,df2,on=['key1','key2'],how='left')
print(dfJoin)

stockPriceData.head()

"""6. Write a Pandas program to create a line plot of the historical stock prices of
Alphabet Inc. between two specific dates.

"""

# A new column CorrectDate is created to hold the parsed (to datetime type) Date column
stockPriceData['CorrectDate'] = pd.to_datetime(stockPriceData['Date'])
# new column is added
stockPriceData.head()
#let date between the required plot is to be plotted are '4/13/2020', '9/14/2020'
dataSD = stockPriceData[(stockPriceData['CorrectDate'] >= '4/13/2020') & (stockPriceData['CorrectDate'] <= '9/14/2020')]
# sorted the data.
dataSDSorted =  dataSD.sort_values(by='CorrectDate')

# plot function is used Date and the Close (price) columns. Here the Close price is assumed to be the historical stock prices of Alphabet is
plt.plot(dataSDSorted['CorrectDate'], dataSDSorted['Close'])

# x and y labeling
plt.xlabel("Date")
plt.ylabel("Closing Price")

"""7. Write a Pandas program to create a line plot of the opening, closing stock prices
of Alphabet Inc. between two specific dates.

"""

dataSD = stockPriceData[(stockPriceData['CorrectDate'] >= '4/13/2020') & (stockPriceData['CorrectDate'] <= '9/14/2020')]
dataSDSorted =  dataSD.sort_values(by='CorrectDate')

# plot function is used to plot Date and the Close & Open (price) columns.
plt.plot(dataSDSorted['CorrectDate'], dataSDSorted['Close'],label="Close")
plt.plot(dataSDSorted['CorrectDate'], dataSDSorted['Open'],label="Open")

# plot legend function is used to distinguish between the label close and open
plt.legend()
plt.title("Close and Open between two specific dates")
plt.xlabel("Date")
plt.ylabel("Closing Price")

"""8. Write a Pandas program to create a bar plot of the trading volume of Alphabet
Inc. stock between two specific dates.

"""

dataSD = stockPriceData[(stockPriceData['CorrectDate'] >= '4/13/2020') & (stockPriceData['CorrectDate'] <= '9/14/2020')]
dataSDSorted =  dataSD.sort_values(by='CorrectDate')
# plot function is used to volume column against two specific dates.
plt.bar(dataSDSorted['CorrectDate'], dataSDSorted['Volume'])

plt.xlabel("Date")
plt.ylabel("Trading Volume")

"""9. Write a Pandas program to create a bar plot of opening, closing stock prices of
Alphabet Inc. between two specific dates.

"""

from re import X
dataSD = stockPriceData[(stockPriceData['CorrectDate'] >= '4/13/2020') & (stockPriceData['CorrectDate'] <= '5/13/2020')]
dataSDSorted =  dataSD.sort_values(by='CorrectDate')

# width of the bar is taken as
bar_width = 0.4
# then 0.2 width should be for the Open price and 0.2 should be for Close price

# to generate all the label locations, using  arrange function (which return evenly spaced values within a given interval)
# generated a list of locations for each entry in the column under the plot.

locations = np.arange(len(dataSDSorted))

print("Length of the dataset =",len(dataSDSorted), "Total width of the bar = ",bar_width)

# left and the right location for all the locations generated above.
X = locations - bar_width / 2
Y = locations + bar_width / 2


# the locations will look like for width 0.4

#x = [-0.2, 0.8,  1.8,  2.8,  3.8,  4.8,  5.8,  6.8,  7.8,  8.8,9.8, 10.8, 11.8, 12.8,
# 13.8, 14.8, 15.8, 16.8, 17.8, 18.8, 19.8, 20.8, 21.8]
#y = [0.2,  1.2,  2.2,  3.2,  4.2,  5.2,  6.2,  7.2,  8.2,  9.2, 10.2, 11.2, 12.2, 13.2,
# 14.2, 15.2, 16.2, 17.2, 18.2, 19.2, 20.2, 21.2, 22.2]

plt.figure(figsize=(12, 6))

plt.bar(X, dataSDSorted['Open'], width=bar_width, color='skyblue', label='Opening Price')
plt.bar(Y, dataSDSorted['Close'], width=bar_width, color='salmon', label='Closing Price')

# To display the date on the x axis, used the xticks function in which the first parameter is locations,
# i.e it will be displayed at the center of each bar
# Further rotation parameter is used to display the date correctly and at an angle so that sufficent space is created between them.
# ha  - parameter is used to horizontally align the x axis data.
plt.xticks(locations, dataSDSorted['CorrectDate'], rotation=45, ha="right")

plt.legend()
plt.title("Open, Close and Volume between two specific dates")

plt.xlabel("Date")
plt.ylabel("Price")

plt.tight_layout()
plt.show()

"""10. Write a Pandas program to create a stacked bar plot of opening, closing stock
prices of Alphabet Inc. between two specific dates.
"""

# stacked parameter is provided so that the both the variables used here (Open and Close) are stacked together.

dataSDSorted[['Open', 'Close']].plot(kind='bar', stacked=True, color=['red', 'blue'], figsize=(12, 6))