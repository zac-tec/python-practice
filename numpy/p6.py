import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(a[0])
print(a[1][2])
print(a[2:3, 2:3]) #last row, last column
print(a[0:2, 0:3]) #first two rows, first three columns    
print(a[::-1]) #reverse the order of the rows
print(a[:, ::-1]) #reverse the order of the columns  
print(a[::-1, ::-1]) #select every other row and column
print(a[0:3:2, 0:3:2])#select every other row and column 
#transpose of the array
print(a.T)
 
