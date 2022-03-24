'''
Array transposition
'''
import numpy as np
from pprint import pprint

arr = np.arange(50).reshape(10,5)
#print("\nArray created is : \n {}".format(arr))
pprint(arr)
print(arr)

print("\nTransposed matrix is: \n {}".format(arr.T))
print("\nDot product of the matrices is : \n{}".format(np.dot(arr,arr.T)))

print("\nMaking 3d matrix")
arr3d = np.arange(50).reshape(5,5,2)
print(arr3d)
print("\n Transposed 3d matrix is : \n {}".format(arr3d.transpose((1,0,2))))

arr1 = np.array([[1,2,3]])
pprint("This array is:{}".format(arr1))
print("Array with axes swapped is:\n{}".format(arr1.swapaxes(0,1)))

