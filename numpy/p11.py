#boolean filtering
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print("elements greater than 5:", a[a > 5])
print("elements less than 5:", a[a < 5])    
print("elements equal to 5:", a[a == 5])
print("even elements:", a[a % 2 == 0])
print("odd elements:", a[a % 2 != 0])
#Replace values < 10 with 0
a[a < 10] = 0
print("array after replacing values < 10 with 0:\n", a)
b=np.arange(-5,11)
print("original array:", b)
b = np.where(b < 0, 0, b)
print("array after replacing values < 0 with 0:\n", b)

