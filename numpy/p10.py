#  axis concepts
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
#make operations along print messages 
print(a)
print("sum of each column:", a.sum(axis=0)) #sum of each column
print("sum of each row:", a.sum(axis=1)) #sum of each row
print("mean of each column:", a.mean(axis=0)) #mean of each column
#row with maximum value in each column
print("row with maximum value in each column:", a.argmax(axis=0))
print("column with maximum value in each row:", a.argmax(axis=1))

