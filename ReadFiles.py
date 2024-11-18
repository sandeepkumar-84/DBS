import pandas as pd
#import csv
#import io
import requests as requests
from io import StringIO



url = "https://github.com/sandeepkumar-84/DBS/blob/practice_prog_da/play_tennis.csv"

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0"}
req = requests.get(url,headers=headers)
data = StringIO(req.text)
x = pd.read_csv(data,sep=",", encoding='utf-8',on_bad_lines='skip')

print(x.head())


'''
url = "https://github.com/sandeepkumar-84/DBS/blob/practice_prog_da/play_tennis.csv"
r = requests.get(url)
buff = io.StringIO(r.text)
dr = csv.DictReader(buff)
for row in dr:
    print(row)
'''


