import requests


def fetch_holidays(countryCode,year):
    country = countryCode
    year = year
    api_url = 'https://api.api-ninjas.com/v1/holidays?country={}&year={}'.format(country, year)
    response = requests.get(api_url, headers={'X-Api-Key': '5AIaxDVRSZ1JOwIr2WqYcw==ZUIPmKonNu5Q5Z4w'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return response


print("Calling holiday API")
res_holidays = fetch_holidays('GB',2010)

print("Response Received")
print(res_holidays.text)


