#Missing Data
#Index hierarchy
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from pprint import pprint

data= Series(['one','two',np.nan,'four'])
print("We have null where bool == True\n{}".format(data.isnull()))
data.dropna()
print("\nDropna does not permanently drop null rows: \n{}".format(data))
dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
print("\nDataframe made is: \n{}".format(dframe))
clean_dframe = dframe.dropna()
print("\nCleaned dframe is: \n{}".format(clean_dframe))
print("Dropping rows where all values are NaN\n{}".format(dframe.dropna(how='all')))
print("Dropping columns where values have NaN\n{}".format(dframe.dropna(axis=1)))
npn = np.nan
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
print(dframe2)
print("\nDrops rows having a minimum 2 not nulls\n{}".format(dframe2.dropna(thresh = 2)))
print("\nDrops rows having a minimum 3 not nulls\n{}".format(dframe2.dropna(thresh = 3)))

print("\nFilling 1 for the nulls \n{}".format(dframe2.fillna(1)))

print("\nFills the null value of particular column with the column no. Made using dictionary. \n{}".format(dframe2.fillna({0:0,1:1,2:2,3:3})))
#dframe2.fillna(0,inplace=True) to permanently change DF

print("Hierarchy and index of index")
from numpy.random import randn
ser = Series(randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
print(ser)
print(ser.index)
print(ser[1])
print(ser[2])
print(ser[:,'a'])
dframe3 = ser.unstack
print(dframe3)
dframe4 = DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['NY','NY','LA','SF'],['cold','hot','hot','cold']])
print(dframe4)
dframe4.index.names=['INDEX_1','INDEX_2']
dframe4.columns.names=['Cities','Temp']
print(dframe4)
print(dframe4.swaplevel('Cities','Temp',axis=1))
#print(dframe4) #not a permanent change
print(dframe4.sort_index(level=1))
print(dframe4.sort_values(by = 'INDEX_2'))
# print(dframe4) not a permanent sbchange
print(dframe4.sum(level='Temp',axis=1))