#Merge and Join, Concatenate Datasets
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

print("\n**********************")
print("Merging of DFs")
print("***********************\n")
#merging by columns
dframe1 = DataFrame({'Key': ['X','Y','Z', 'Z','X','X'],'data_set_1':np.arange(6)})
print(dframe1)
dframe2 = DataFrame({'Key':['Q','Y','Z'],'data_set_2':[1,2,3]})
print(dframe2)
dframe3 = pd.merge(dframe1,dframe2) #many to one merge
print(dframe3) 
dframe4 = pd.merge(dframe1,dframe2,on='Key',how = 'left') #Left/Right join
print(dframe4)
dframe5 = pd.merge(dframe1,dframe2,on='Key',how = 'outer') #union od datasets
print(dframe5)

dframe_left = DataFrame({'key1':['SF','SF','LA'], 'key2':['one','two','one'], 'left_data':[1,2,3]})
dframe_right = DataFrame({'key1':['SF','LA','LA'], 'key2':['one','one','one'], 'right_data':[5,6,7]})
dframe6 = pd.merge(dframe_left,dframe_right,on=['key1','key2'],how='outer') #many to many join
print(dframe6) 

#merging on index
df_left = DataFrame({'key':['X','Y','Z','X','Y'],'data':range(5)})
df_right = DataFrame({'group_data':[10,20]},index=['X','Y'])
dframe7 = pd.merge(df_left,df_right,left_on='key',right_index=True)
print(dframe7)

#index hierarchy example:
df1_left = DataFrame({'key1':['SF','SF','SF','LA','LA'], 'key2':[10,20,30,20,30], 'data_set':range(5)})
print("\nThe left dataset for index hierarchy example is: \n{}".format(df1_left))
df1_right = DataFrame(np.arange(10).reshape(5,2),index = [['LA','LA','LA','SF','SF'],[10,20,10,10,20]],columns = ['col_1','col_2'])
print("\nThe right dataset for index hierarchy example is: \n{}".format(df1_right))
df_merge = pd.merge(df1_left,df1_right,left_on=['key1','key2'],right_index=True, how='outer')
print("\nThe merged dataset is: \n{}".format(df_merge))

#Using join
df1_merge = df_left.join(df_right)
print("\nThe merged dataset using join is: \n{}".format(df1_merge))
print(df_left)
print(df_right)

#using np.concatenate - this covers only arrays and series or pd.concat - this covers DFs, Series
print("\n**********************")
print("Concatenation of Arrays, Series, matrices and DFs")
print("***********************\n")

arr1 = np.arange(9).reshape(3,3)
arr2 = arr1
concat_arr = np.concatenate([arr1,arr2])
print("\nThe concatenated array is: \n{}".format(concat_arr))

ser1 = Series([0,1,2],index=['X','Y','Z'])
ser2 = Series([3,4],index=['A','B'])
concat_ser = pd.concat([ser1,ser2],axis=0)
print("\nThe concatenated series is: \n{}".format(concat_ser))
#changing axis=1 produces a DF instead
concat_ser_withkeys = pd.concat([ser1,ser2],axis=0, keys=['Cat1','Cat2'])
print("\nThe concatenated series with keys is: \n{}".format(concat_ser_withkeys))

dframe1 = DataFrame(np.random.randn(4,3), columns=['X','Y','Z'])
dframe2 = DataFrame(np.random.randn(3,3), columns=['X','Y','Q'])
print(dframe1)
print(dframe2)
concat_dframe = pd.concat([dframe1,dframe2])
print("\nThe concatenated DF is: \n{}".format(concat_dframe))
#can ignore the left side index using ignore_index = True that gives proper DF counting 0,1,2,3,4,5...
