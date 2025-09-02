import numpy as np
import matplotlib.pyplot as plt

m = 0
sd = 1
data = np.random.normal(loc=m, scale=sd, size=1000)

x = np.arange(1000) 
plt.scatter(x, data, s=5)

plt.title("Scatter Plot of Normal Distribution")
plt.xlabel("Index")
plt.ylabel("Value")

plt.grid(True)
plt.show()



