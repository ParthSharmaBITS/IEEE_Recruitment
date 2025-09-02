import numpy as np
import matplotlib.pyplot as plt

m = 0 # mean
sd = 1 # standard deviation
data = np.random.normal(loc=m, scale=sd, size=1000) # generate 1000 random numbers from a normal distribution

x = np.arange(1000) # x values from 0 to 999
plt.scatter(x, data, s = 3) # scatter plot with point size 3

plt.title("Scatter Plot of Normal Distribution")
plt.xlabel("Index")
plt.ylabel("Value")

plt.grid(True) # add grid
plt.show() # display the plot




