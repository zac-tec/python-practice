#sorting and searching solutions
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(np.sort(a, axis=0)) #sort each column
print(np.sort(a, axis=1)) #sort each row
b=(np.sort(a, axis=None)) #sort the entire array
print("sorted array:", b)
print(np.argsort(a, axis=0)) #indices of the sorted array along each column
print(np.argsort(a, axis=1)) #indices of the sorted array along each row
uniqe, index = np.unique(a, return_index=True) #unique values and their indices
print("unique values:", uniqe)
print("indices of unique values:", index)   