import random
import numpy as np  

arr = np.random.randint(1, 100, size = (5,5))  
sl_arr = arr[1:4, 1:4]  # Slices the array to get the 3x3 array from the center

print(f"Original array:\n{arr}\nSliced array:\n{sl_arr}")

fr = sl_arr[0] # First row of the sliced array
lc = sl_arr[:,2] # Last column of the sliced array

print(f"Dot product of first row and last column:\n{np.dot(fr, lc)}") # Prints the dot product 