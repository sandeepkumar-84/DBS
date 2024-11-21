import HolidaysInfoEntity
import DatabaseHandling

list_holidays = HolidaysInfoEntity.holiday_main()

print("Checking database connection.................")
#DatabaseHandling.db_check_connection()
print("Creating database .................")
DatabaseHandling.db_create_db()

print("Creating table .................")
DatabaseHandling.db_create_table_holiday()

print("Populating table .................")
DatabaseHandling.db_populate_table_holiday(list_holidays)


