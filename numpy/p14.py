#broadcasting solutions
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.array([1,2,3])
print(a+b) #broadcasting addition
print(a*b) #broadcasting multiplication
print(a/b) #broadcasting division
print(a**b) #broadcasting exponentiation
print(a%b) #broadcasting modulo
#vector with different shape

b = np.array([10,20,30])

print(a + b)
#Subtract column vector from matrix


b = np.array([[5],
              [10],
              [15]])

print(a - b)  
#noramalize the array
normalized_a = (a - np.mean(a)) / np.std(a)
print("normalized array:\n", normalized_a)  