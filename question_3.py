import random
import numpy as np  

arr = np.random.randint(1, 100, size = (5,5))  # Creates a 5x5 array with random integers from 1 to 100
max = np.max(arr) 
min = np.min(arr)
mean = np.mean(arr)  # These functions compute the max, min, and mean of the array

print(f"Array:\n{arr}\nMaximum: {max}\nMinimum: {min}\nMean: {mean}")

new_arr = arr/100 # Divides each element by 100 causing it to be in the range 0-1
new_arr = np.sort(new_arr.flatten()) # Flattens the array to 1D and sorts it
print(f"Flattened Array:\n{new_arr}")