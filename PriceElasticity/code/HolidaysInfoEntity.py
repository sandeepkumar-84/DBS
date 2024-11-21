import json
import os
import requests

fresh_api_call = True

def fetch_holidays(countryCode,year):
    country = countryCode
    year = year
    api_url = 'https://api.api-ninjas.com/v1/holidays?country={}&year={}'.format(country, year)
    response = requests.get(api_url, headers={'X-Api-Key': '5AIaxDVRSZ1JOwIr2WqYcw==ZUIPmKonNu5Q5Z4w'})
    if response.status_code == requests.codes.ok:
        print("response received from API...")        
    else:
        print("Error:", response.status_code, response.text)
    return response

def get_saved_holiday_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return None  # Return None if file is missing
    try:

        with open(filepath, "r") as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def save_holiday_into_file(filepath,inputData):
    with open(filepath, "w") as json_file:
        json.dump(inputData, json_file, indent=4)
        print(f"JSON data saved to {filepath}")

class HolidayListInfo:
    def __init__(self, country, iso, year, date, day, name, type):
        self.country = country
        self.iso = iso
        self.year = year
        self.date = date
        self.day = day
        self.name = name
        self.type = type

    @classmethod
    def get_holiday_list_cls(cls, input_json_data):
        #desiarlize the input json        
        return cls(
            country=input_json_data.get("country"),
            iso=input_json_data.get("name"),
            year=input_json_data.get("price"),
            date=input_json_data.get("date"),
            day=input_json_data.get("day"),
            name=input_json_data.get("name"),
            type=input_json_data.get("type"),
        )

    def __repr__(self):
        return f"HolidayListInfo(country={self.country}, iso={self.iso}, year={self.year}, date={self.date}, day={self.day}, name={self.name}, type={self.type})"
    
    def combine(self, other):
        if not isinstance(other, HolidayListInfo):
            raise ValueError("Can only combine with another HolidayListInfo object")        
        
        combined_stock = self.stock + other.stock
        combined_price = max(self.price, other.price)
        return HolidayListInfo(self.product_id, self.name, combined_price, combined_stock)

    
def get_loaded_holiday_text(file_path,country,year):
    holiday_json_api_res_text1 = get_saved_holiday_file(file_path)
    if fresh_api_call == False and holiday_json_api_res_text is not None:
        print("Loaded data from local\n")
    else:
        print(f"Failed to load JSON data from local path {file_path}\n")
        print("Calling API to fetch the data")
        holiday_json_api_res = fetch_holidays(country,year)
        if holiday_json_api_res.status_code == requests.codes.ok:
            holiday_json_api_res_text1 = holiday_json_api_res.text
            print("Saving into the file on local system")
            save_holiday_into_file(file_path,holiday_json_api_res.text)
        else:
            print("Failed to fetch from API") 
    return holiday_json_api_res_text1   

def get_loaded_holiday_class(holiday_json_api_res_text2):
    ## Fetching the holidays, saving it into local 
    print("Loading resonse into JSON object")
    res = json.loads(holiday_json_api_res_text2)
    holidays = [HolidayListInfo.get_holiday_list_cls(item) for item in res]
    return holidays

def fetch_date_df(holidays):
    listHolidayList = []
    for items in holidays:
      listHolidayList.append(items.date)  
    return listHolidayList


#######################  Main Execution ####################
dates_holiday = []

def holiday_main():
    file_path = r"C:\holiday_data_2010.json"
    country = "GB"
    year = 2010

    holiday_json_api_res_text =  get_loaded_holiday_text(file_path,country,year)
    print(f"Converting to class object for year {year}")
    holidays_2010 = get_loaded_holiday_class(holiday_json_api_res_text)

    file_path = r"C:\holiday_data_2010.json"
    country = "GB"
    year = 2011

    holiday_json_api_res_text =  get_loaded_holiday_text(file_path,country,year)
    print(f"Converting to class object for year {year}")
    holidays_2011 = get_loaded_holiday_class(holiday_json_api_res_text)

    holidays_comb = holidays_2010 + holidays_2011



    print("Printing class object\n")

    '''
    for items in holidays_2010:
        print(f"country = {items.country}, iso={items.iso}, year={items.year}, date={items.date}, day={items.day}, name={items.name}, type={items.type}")
    for items in holidays_2011:
        print(f"country = {items.country}, iso={items.iso}, year={items.year}, date={items.date}, day={items.day}, name={items.name}, type={items.type}")
    '''

    for items in holidays_comb:
        print(f"country = {items.country}, iso={items.iso}, year={items.year}, date={items.date}, day={items.day}, name={items.name}, type={items.type}")
        
    dates_holiday = fetch_date_df(holidays_comb)

    print(f"List of holidays year 2010 and 2011\n")


    for items in holidays_comb:
        print(items.date)
    
    return dates_holiday


holiday_main()


