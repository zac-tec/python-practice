#COMBINING & SPLITTING — SOLUTIONS
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([[10,11,12],
              [13,14,15],
              [16,17,18]])
#vertical stacking  
print("vertical stacking:\n", np.vstack((a,b)))
#horizontal stacking
print("horizontal stacking:\n", np.hstack((a,b)))
split_a = np.array_split(a, 3) #split into 3 equal parts
print("split into 3 equal parts:\n", split_a)
split_b = np.array_split(a, 2) #split into 2 equal parts
print("split into 2 equal parts:\n", split_b) 

a = np.array([1,2,3,4,5,6,7,8,9])
print(np.array_split(a, 3))