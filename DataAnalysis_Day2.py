'''Data Analysis and Visualisation - Numpy, Pandas, Import and export data and Visualise (Matplotlib, seaborn)
Numpy - Scientific computing
Pandas - series, DF, Data analysis
JSON, HTML, CSV, EXCel
Pol election dataset, 
ML - SciKit Learn
Stats - 
SQLAlchemy 
Web Scrapping : Bful Soup'''

print("\n*************************")
print("\nUSING ARRAYS AND SCALARS")
print("\n*************************")

import numpy as np
arr1 = np.array([[1,2,3,4],[8,9,10,11]])
print("\nMultiplying: \n{}".format(arr1*arr1))
print("\nSubtraction : \n{}".format(arr1-arr1))
print("\nInverse Array : \n{}".format(1/arr1))

print("\n*************************")
print("\nINDEXING ARRAYS")
print("\n*************************")
arr = np.arange(0,11)
print(arr)
print(arr[8])
print("\nGetting values in array : {}".format(arr[1:5]))
arr[0:5] = 100
print("\nSetting values: {}".format(arr))

arr = np.arange(0,11)
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99
print("Slice of array : {}".format(slice_of_arr))
print("Original array changed : {}".format(arr))

arr = np.arange(0,11)
arr_copy = arr.copy()
print("To avoid overwriting : {}".format(arr_copy))

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print("\nCalling a row: {}".format(arr_2d[1]))
print("\nIndividual element: {}".format(arr_2d[1][1]))
print("\nSlicing again: Everything above 2nd row and beyond 1st columns \n{}".format(arr_2d[:2,1:]))

arr2dzero = np.zeros([10,10])
print("\n---------Changing values of array-------")
for i in range(arr2dzero.shape[1]):
	arr2dzero[i]=i
print("\nFancy indexing:\n {}".format(arr2dzero[[6,4,7]]))

