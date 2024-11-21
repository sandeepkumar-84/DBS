import csv
import os
import psycopg2
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

db_host = config['database']['host']
db_port = config.getint('database', 'port')  # Get as integer
db_user = config['database']['username']
db_password = config['database']['password']
db_database = config['database']['db']

base_path = config['basepath']['assignment_path']
ds_directory = config['ds_dir']['cafe_item_dir']

online_retail_ds_file_name = config['datasetFileName']['online_retail_ds_file_name'] 
online_retail_ds_file_path = os.path.join(base_path, ds_directory, online_retail_ds_file_name)



#establish a connection with POSTGRESQL

def db_check_connection():
    try:
        connection = psycopg2.connect(
                database=db_database,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
        print("Connection successful")
        return connection
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)
        
def db_create_db():
    try:    
        conn = psycopg2.connect(dbname="postgres", user=db_user, password=db_password)
        conn.autocommit = True  # Allow non-transactional commands
        cur = conn.cursor()

        # Check if the database exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_database}'" )
        if not cur.fetchone():
            # Create the database if it doesn't exist
            cur.execute(f"CREATE DATABASE {db_database} OWNER postgres")
            print(f"Database {db_database} created.")
        else:
            print(f"Database {db_database} already exists.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)

def db_create_table_holiday():    
    try:
        connection = db_check_connection()
        
        #extract data from database store in the variable
        cursor_obj = connection.cursor()
        
        #create table for  holiday list into postgreSQL
        cursor_obj.execute("""
                        CREATE TABLE IF NOT EXISTS tbl_holiday_list (
                            holiday_date varchar(20)
                        )
        """)
        connection.commit()
        cursor_obj.close()
        connection.close()

        print(f"Table tbl_holiday_list created sucessfully")        
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)  


def db_populate_table_holiday(dates_holiday):    
    try:
        connection = db_check_connection()
        
        #extract data from database store in the variable
        cursor_obj = connection.cursor()
        
        truncate_table = "TRUNCATE TABLE sales_data;"
        cursor_obj.execute(truncate_table)
        connection.commit()

        for items in dates_holiday:
            cursor_obj.execute(
        "INSERT INTO tbl_holiday_list (holiday_date) VALUES (%s)", (str(items),)
    )                    

        connection.commit()
        cursor_obj.close()
        connection.close()

        print(f"Table tbl_holiday_list populated sucessfully")        
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)

def db_create_table_retail_online():    
    try:
        connection = db_check_connection()
        
        #extract data from database store in the variable
        cursor_obj = connection.cursor()
        
        #create table for  holiday list into postgreSQL
        cursor_obj.execute("""
                        CREATE TABLE IF NOT EXISTS  sales_data (
                                                    InvoiceNo VARCHAR(20),
                                                    StockCode VARCHAR(20),
                                                    Description TEXT,
                                                    Quantity INT,
                                                    InvoiceDate TIMESTAMP,
                                                    UnitPrice DECIMAL(10, 2),
                                                    CustomerID VARCHAR(20),
                                                    Country VARCHAR(50)
                                                )
                        """)
        connection.commit()
        cursor_obj.close()
        connection.close()

        print(f"Table sales_data created sucessfully")        
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)  


def db_populate_table_retail_online():    
    try:
        connection = db_check_connection()
        
        #extract data from database store in the variable
        cursor_obj = connection.cursor()
        
        truncate_table = "TRUNCATE TABLE sales_data;"
        cursor_obj.execute(truncate_table)
        connection.commit()
        #insert data from csv file to table tbl_cafeItem
        with open(online_retail_ds_file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cursor_obj.execute(
                    "INSERT INTO sales_data(InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)",
                    row
                )
        connection.commit()        
                         

        connection.commit()
        cursor_obj.close()
        connection.close()

        print(f"Table sales_data populated sucessfully")        
    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)        

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==================
      