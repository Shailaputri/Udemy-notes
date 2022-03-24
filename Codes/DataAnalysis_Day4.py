'''
Universal Array Functions
'''
import numpy as np
arr = np.arange(11)
print("\n Square root of array is \n{}".format(np.sqrt(arr)))
print("\n Square root of array is \n{}".format(np.exp(arr)))
print("\nBinary Functions on 2 arrays")
A = np.random.randn(10)
B = np.random.randn(10)
print("\nAdded array is: \n{}".format(np.add(A,B)))
print("\nMax array is: \n{}".format(np.maximum(A,B)))

website = "http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
import webbrowser
webbrowser.open(website)

