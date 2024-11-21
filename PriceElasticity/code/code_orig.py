#install important libraries
#pip install psycopg2 pandas numpy matplotlib seaborn scikit-learn scipy lightgbm
#import library to connect to postgresql database
import psycopg2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime


#to change the format of date columns stored in csv file
def date_format(all_date):
    for fmt in ('%m/%d/%Y', '%Y-%m-%d', '%B %d, %Y', '%d-%m-%Y', '%m-%d-%Y', '%Y.%m.%d', '%d-%b-%Y', '%B %d %Y'):
        try:
            return datetime.strptime(all_date, fmt).date() 
        except ValueError: 
            continue 
    raise ValueError(f"Date format for '{all_date}' is not recognized")


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==================
#establish a connection with POSTGRESQL
try:
    connection = psycopg2.connect(
        database="cafeDB",
        user="postgres",
        password="1234567890",
        host="localhost",
        port="5432"
    )
    print("Connection successful")

    #extract data from database store in the variable
    cursor_obj = connection.cursor()
    
    #create table for cafe item into postgreSQL
    cursor_obj.execute("""
                    CREATE TABLE IF NOT EXISTS tbl_cafeItem (
                    sell_id INTEGER,
                    sell_category INTEGER,
                    item_id INTEGER,
                    item_name VARCHAR(255)
                    )
    """)
    connection.commit()
    truncate_table = "TRUNCATE TABLE tbl_cafeItem;"
    cursor_obj.execute(truncate_table)
    connection.commit()
    #insert data from csv file to table tbl_cafeItem
    with open('C:/Users/NITS/Desktop/PriceElasticity_datasets/cafe_item.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor_obj.execute(
                "INSERT INTO tbl_cafeItem (sell_id, sell_category, item_id, item_name) VALUES (%s, %s, %s, %s)",
                row
            )
    connection.commit()
    
    #create table for cafe transaction into postgreSQL
    cursor_obj.execute("""
                    CREATE TABLE IF NOT EXISTS tbl_cafeTransaction (
                    calendar_date DATE ,
                    price FLOAT,
                    quantity INTEGER,
                    sell_id INTEGER,
                    sell_category INTEGER 
                    )
    """)
    connection.commit()
    truncate_table = "TRUNCATE TABLE tbl_cafeTransaction;"
    cursor_obj.execute(truncate_table)
    connection.commit()
    #insert data from csv file to table tbl_cafeTransaction 
    with open('C:/Users/NITS/Desktop/PriceElasticity_datasets/cafe_transaction.csv', 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1) #ignore header row
        for row in reader1:
            #parse the date
            formatted_date = date_format(row[0])
            
            cursor_obj.execute(
                "INSERT INTO tbl_cafeTransaction (calendar_date, price, quantity, sell_id, sell_category) VALUES (%s, %s, %s, %s, %s)",
                (formatted_date, row[1], row[2], row[3], row[4])
            )
    connection.commit()

    #create table for cafe infodate into postgreSQL
    cursor_obj.execute("""
                    CREATE TABLE IF NOT EXISTS tbl_cafeInfoDate (
                    calendar_date DATE ,
                    year INTEGER,
                    holiday VARCHAR(255),
                    is_weekend INTEGER,
                    is_schoolbreak INTEGER, 
                    average_temperature FLOAT,
                    is_outdoor INTEGER
                    )
    """)
    connection.commit()
    truncate_table = "TRUNCATE TABLE tbl_cafeInfoDate;"
    cursor_obj.execute(truncate_table)
    connection.commit()
    #insert data from csv file to table tbl_cafeInfoDate
    with open('C:/Users/NITS/Desktop/PriceElasticity_datasets/cafe_infodate.csv', 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2) #ignore header row
        for row in reader2:
            #parse the date
            formatted_date = date_format(row[0])
            
            cursor_obj.execute(
                "INSERT INTO tbl_cafeInfoDate (calendar_date, year, holiday, is_weekend, is_schoolbreak, average_temperature, is_outdoor) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (formatted_date, row[1], row[2], row[3], row[4], row[5], row[6])
            )
    connection.commit()
#LOAD THE DATA to DATAFRAME
    def fetch_to_dataframe(query):
        cursor_obj.execute(query)
        columns = [desc[0] for desc in cursor_obj.description]
        data = cursor_obj.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df
    
    query1 = "SELECT * FROM tbl_cafeItem" 
    query2 = "SELECT * FROM tbl_cafeTransaction"
    query3 = "SELECT * FROM tbl_cafeInfoDate"

    df_cafeItem = fetch_to_dataframe(query1)
#  print(df_cafeItem)
    df_cafeTransaction = fetch_to_dataframe(query2)
#    print(df_cafeTransaction)
    df_cafeInfoDate = fetch_to_dataframe(query3)
#    print(df_cafeInfoDate)

    truncate_table = "TRUNCATE TABLE tbl_cafeInfoDate;"
    cursor_obj.execute(truncate_table)
    connection.commit()
    #insert data from csv file to table tbl_cafeInfoDate
    with open('C:/Users/NITS/Desktop/PriceElasticity_datasets/cafe_infodate.csv', 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2) #ignore header row
        for row in reader2:
            #parse the date
            formatted_date = date_format(row[0])
            
            cursor_obj.execute(
                "INSERT INTO tbl_cafeInfoDate (calendar_date, year, holiday, is_weekend, is_schoolbreak, average_temperature, is_outdoor) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (formatted_date, row[1], row[2], row[3], row[4], row[5], row[6])
            )
    connection.commit()
#LOAD THE DATA to DATAFRAME
    def fetch_to_dataframe(query):
        cursor_obj.execute(query)
        columns = [desc[0] for desc in cursor_obj.description]
        data = cursor_obj.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df
    
    query1 = "SELECT * FROM tbl_cafeItem" 
    query2 = "SELECT * FROM tbl_cafeTransaction"
    query3 = "SELECT * FROM tbl_cafeInfoDate"

    print("Loading the data into dataframes\n")
    print("Cafe Item Data Frame")
    df_cafeItem = fetch_to_dataframe(query1)
#  print(df_cafeItem)
    print("Cafe Item Transaction Data Frame")
    df_cafeTransaction = fetch_to_dataframe(query2)
#    print(df_cafeTransaction)
    print("Cafe Item Info Date Data Frame")
    df_cafeInfoDate = fetch_to_dataframe(query3)
#    print(df_cafeInfoDate)

    # Close the cursor and connection
    cursor_obj.close()
    connection.close()
    print("Connection Closed")

except Exception as e:
    print("Error while connecting to PostgreSQL:", e)

#=============================================================
#Data Cleaning
#print(df_cafeItem.head())
#print(df_cafeInfoDate.head())
#print(df_cafeTransaction.head())
#detecting and dropping missing values if any
print(df_cafeItem.isnull().sum())
df_cafeItem.dropna(inplace=True)
print(df_cafeInfoDate.isnull().sum())
df_cafeInfoDate.dropna(inplace=True)
print(df_cafeTransaction.isnull().sum())
df_cafeTransaction.dropna(inplace=True)

#remove duplicates if any
df_cafeItem.drop_duplicates(inplace=True)
df_cafeTransaction.drop_duplicates(inplace=True)
df_cafeInfoDate.drop_duplicates(inplace=True)

#checking for outliers
Q1 = df_cafeTransaction['price'].quantile(0.25)
Q3 = df_cafeTransaction['quantity'].quantile(0.75)
IQR = Q3-Q1
#df_cafeTransaction = df_cafeTransaction[((df_cafeTransaction['price'] < (Q1 - 1.5 * IQR)) |(df_cafeTransaction['price'] > (Q3 + 1.5 * IQR)))]
#df_cafeTransaction = df_cafeTransaction[(df_cafeTransaction['price']<(Q1 - 1.5*IQR)) | ((df_cafeTransaction['price']>(Q3 + 1.5*IQR)))]
plt.figure(figsize=(10, 6)) 
sns.boxplot(data=df_cafeTransaction) 
plt.title('Box Plot for df_cafeTransaction') 
plt.show()

#df_cafeItem
#sell_id: categorical variable, identification of combination of items
#sell_category: "0" identifies single item product
#                "1" identifies combo product
#item_id: categorical variable, identifier of single item
#item_name: categorical variable, contains name of product
sns.pairplot(df_cafeItem)
plt.show()

#df_cafeTransaction
#calendar_date: contains transaction date
#price: states the product price correlated with sell_id
#quantity: number of product sold
#sell_id: identifier of product which is sold
#sell_category: category of product sold
plt.hist(df_cafeTransaction.price, edgecolor='black')
plt.show()
sns.pairplot(df_cafeTransaction)
plt.show()

#df_cafeInfoDate
print(df_cafeInfoDate.columns)
print(df_cafeInfoDate.dtypes)
df_cafeInfoDate['holiday'] = df_cafeInfoDate['holiday'].replace('NULL','Working Day')
print(df_cafeInfoDate)
sns.pairplot(df_cafeInfoDate)

#
print(np.unique(df_cafeInfoDate['holiday']))

print(pd.concat([df_cafeItem.sell_id, pd.get_dummies(df_cafeItem.item_name)], axis=1).groupby(df_cafeItem.sell_id).sum())

merge_data1 = pd.merge(df_cafeItem.drop(['item_id'],axis=1), df_cafeTransaction.drop(['sell_category'],axis=1), on='sell_id')
print(merge_data1.head(10))
group_data1 = merge_data1.groupby(['sell_id','sell_category','item_name','calendar_date','price']).quantity.sum()
print(group_data1)
print(group_data1.shape)


