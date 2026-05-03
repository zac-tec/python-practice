#flatten a array
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a.reshape(-1))#reshape the array to 2 rows and 5 columns
print(a.flatten())
print(a.ravel())
print(a[1][2])
print(a[:,:])