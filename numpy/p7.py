#make transpose of a matrix 3x3 without using built in function

import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]]) 
print(a) 

   
transpose = np.zeros((a.shape[1], a.shape[0]), dtype=a.dtype)  # Create an empty array for the transpose
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        transpose[j][i] = a[i][j]  # Assign the transposed values
print(transpose)        