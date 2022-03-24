#Array input and output
import numpy as np
arr = np.arange(5)
np.save('myarray',arr)
arr = np.arange(10)
print("\nLoad Save arrays as numpy {}".format(np.load('myarray.npy')))

arr1 = np.load('myarray.npy')
arr2 = arr
np.savez('ziparray.npz', x=arr1, y=arr2)
archive_array = np.load('ziparray.npz')
print("\nLoad Save arrays as zip {}".format(archive_array['x']))

arrmat = np.array([[1,2,3],[4,5,6]])
print("\n Creating an array matrix 2*3: \n{}".format(arrmat))


np.savetxt('mytextarray.txt',arrmat,delimiter = ',')
arrmat_stored = np.loadtxt('mytextarray.txt',delimiter = ',')
print("\nLoad Save arrays as text: \n{}".format(arrmat_stored))
