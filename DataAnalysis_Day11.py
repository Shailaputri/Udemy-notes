#Data Analysis- Reading/Writing files
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint

dframe = pd.read_csv('lec25.csv')
print("Command to view DF\n{}".format(dframe))
dframe = pd.read_csv('lec25.csv',header=None)
print("\nCommand to show index of columns of DF \n{}".format(dframe))
dframe = pd.read_table('lec25.csv',sep = ",", header = None)
print("\nMore generic way to read CSV by explicitly providing the delimiter/separator\n{}".format(dframe))
dframe1 = pd.read_csv('lec25.csv',header=None, nrows = 2)
print("\nShows only first two rows: \n{}\n".format(dframe1))
dframe.to_csv("mytextfile.csv")

#to check output here
import sys
dframe.to_csv(sys.stdout)
print("\nTo view the file separated from a cstom separator we have:")
dframe.to_csv(sys.stdout, sep = 'ß')
print("\nTo view only the last two columns we have:")
dframe.to_csv(sys.stdout, sep='_',columns = [3,4])

print("\n**********************")
print("Reading from json")
print("***********************\n")
json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""
import json
data=json.loads(json_obj)
print(data)
# json.dumps(data)
dframe2 = DataFrame(data['food'])
print("\n")
print(dframe2)

print("\n**********************")
print("Reading from html")
print("***********************\n")

from pandas import read_html

# url = 'http://www.fdic.gov/bank/individual/failed/banklist.html' gives no tables exist as the page is redirecting
url='https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dframe_list = pd.io.html.read_html(url)

dframe3 = dframe_list[0]
#pprint(dframe3)
print(dframe3.columns.values)


print("\n**********************")
print("Reading from Excel files")
print("***********************\n")
xlsfile = pd.ExcelFile('Lec_28_test.xlsx')
dframe4 = xlsfile.parse('Sheet1')
print(dframe4)





