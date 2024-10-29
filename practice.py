import re
import pandas as pd

def remove_punctuations(value):
    return re.sub('[!#?]', '', value)

funcs = [str.strip,remove_punctuations,str.title]

cities = ["#newyork", "paris", " france "]

def clean_strings(strInput,functs):
    result = []
    for value in strInput:
        for f in funcs:
            value = f(value)
        result.append(value)

    return result
        


print(clean_strings(cities,funcs))


obj = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


print("pd series:", obj)


data = {
    "state":["Delhi","Mumbai","Chennai","Hyderabad","Calcutta","Assam"],
    "year":["2002","2004","2006","2002","2004","2006"],
    "pop":[1.2,2.2,0.9,1.2,2.2,0.9]
}

frm = pd.DataFrame(data);

print(frm)


frm2 = pd.DataFrame(data,columns=['year','state','pop','debt'], index=['a','b','c','d','e','f'])

colDebt = pd.Series([8,5,3],index=['a','b','c'])
frm2['debt'] = colDebt
x = ['state','year']
y = ['a','b','c']
print(frm2[x])

print(frm2[:'e'])

print("Iloc")
print(frm2.iloc[2,[2,3]])
print("Iloc-2")
print(frm2.iloc[[1,2],[2,3]])

print("loc")
print(frm2.loc[['a','b'],['pop','debt']])





data1 = {
        "a":[1,3,2,4,5],
        "b":[2,3,4,5,6],
        "c":[1,1,2,2,3]
}


df1 = pd.DataFrame(data1,columns=['a','b','c'])

data2 = {
        "a":[1,3,2,4,5],
        "b":[2,3,4,5,6],
        "c":[1,1,2,2,3]
}


df2 = pd.DataFrame(data1,columns=['a','b'])

print(df1)

print(df1.add(df2))
print(df1.add(df2,fill_value=0))


#Existing dataframe
std_data = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
        'marks': [200, 210, 190, 222, 199]}
std_df = pd.DataFrame(std_data)

print("Existing dataframe")
print(std_df)

new_std = {'student_id':['S6'], 'name':['Scarlette Fisher'], 'marks':[205]}

std_df.append(new_std, ignore_index=True)

print("Appended dataframe")
print(std_df)
