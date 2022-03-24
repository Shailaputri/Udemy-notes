'''Data Analysis and Visualisation - Numpy, Pandas, Import and export data and Visualise (Matplotlib, seaborn)
Numpy - Scientific computing
Pandas - series, DF, Data analysis
JSON, HTML, CSV, EXCel
Pol election dataset, 
ML - SciKit Learn
Stats - 
SQLAlchemy 
Web Scrapping : Bful Soup'''

import numpy as np

print("\n*************************")
print("\nCREATING ARRAYS")
print("\n*************************")
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print("\nMaking an array:{}".format(my_array1))
my_list2 = [11,22,33,44]
my_lists = [my_list1,my_list2]
print("\nList for making multiD array:{}".format(my_lists))
my_array2 = np.array(my_lists)
print("\nMaking a multiD array: {}".format(my_array2))
print("\nSize of the multiD array:{}".format(my_array2.shape))

print("\nType of objects in array: {}".format(my_array2.dtype))

my_zeros_array = np.zeros(5)
print("\nCreating an array of zeros: {}".format(my_zeros_array))

my_ones_array = np.ones([5,5])
print("\nCreating multiD array of ones: {}".format(my_ones_array))

my_empty_array = np.empty(5)
print("\nCreating empty array: {}".format(my_empty_array))

my_identity_matrix = np.eye(5)
print("\nCreating identity matrix:\n {}".format(my_identity_matrix))

print(np.arange(5))
print(np.arange(5,50,2))
