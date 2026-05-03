import numpy as np

# Create an array from 1 to 20
a=np.arange(1,21)
print(a)  
print(a.astype(float))
print(a)    # Set data type to integer        
print(a.shape)       # Shape of the array
print(a.ndim)  # Number of dimensions
a = a.astype(bool)  # Convert to boolean

print(a)            
print(a.dtype)# Data type of the array   


# Create 10 numbers between 0 and 5
b=np.linspace(.5,5,10)
print(b.round(2))

# Create a 4×4 matrix filled with 9
c=np.array([[9,9,9,9],[9,9,9,9],[9,9,9,9],[9,9,9,9]])
print(c.ndim)
print(c.shape)
print(c)
print(c.size)

d=np.full((4,4,4),0)
print(d.ndim)
print(d.shape)
print(d.size)

print(d)

# Generate 12 random integers between 50–100
e=np.random.randint(50,101,12)  
print(e)
# 5. Create even numbers from 2 to 50
f=np.arange(2,51,20)
print(f)

# Convert this into:
# 3×4 matrix
# print shape
# convert to float
a = np.arange(1, 13)
a = a.reshape(3,4)
print(a)
print(a.shape)
a = a.astype(float)
print(a)            