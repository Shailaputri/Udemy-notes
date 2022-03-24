#Series
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#Series is an indexed array
obj = Series([3,6,9,12])
print("\nExample of series:\n{}".format(obj))
print("\nValue in series:\n{}".format(obj.values))
print("\nIndex in series: \n{}".format(obj.index))
ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])
print("\nExample of Series with named index \n{}".format(ww2_cas))
print("\nSeries with index USA \n{}".format(ww2_cas['USA']))
#Check which countries had casualties >4mn
print("\n {}".format(ww2_cas[ww2_cas > 4000000]))
print('USSR' in ww2_cas)
ww2_dict = ww2_cas.to_dict()
print(ww2_dict)
ww2_series = Series(ww2_dict)
print(ww2_series)
countries = ['China','Germany','Japan','USA','USSR','Argentina']
obj2 = Series(ww2_dict,index=countries)
print(obj2)
print(pd.isnull(obj2))
print(pd.notnull(obj2))
print(ww2_series + obj2)
obj2.name = 'World War 2 Casualties'
obj2.index.name = 'Countries'
print(obj2)
