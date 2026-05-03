import time 
import numpy as np

lst = list(range(1000000))
arr = np.array(lst)

start = time.time()
[x*2 for x in lst]
print("List:", time.time() - start)

start = time.time()
arr * 2
print("NumPy:", time.time() - start)