import HolidaysInfoEntity
import DatabaseHandling

list_holidays = HolidaysInfoEntity.holiday_main()

print("Checking database connection.................")
#DatabaseHandling.db_check_connection()
print("Creating database .................")
DatabaseHandling.db_create_db()

print("Creating table holiday .................")
DatabaseHandling.db_create_table_holiday()

print("Populating table holiday.................")
DatabaseHandling.db_populate_table_holiday(list_holidays)

print("Creating table sales_data .................")
DatabaseHandling.db_create_table_retail_online()

print("Populating table sales_data.................")
DatabaseHandling.db_populate_table_retail_online()

print("Load tables into datasets.................")
df_sales, df_holiday = DatabaseHandling.load_datasets()

print(f"froma main............{df_sales.shape}")
print(f"froma main............{df_holiday.shape}")
