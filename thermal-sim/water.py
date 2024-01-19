# Numerical simulation of heat diffusion of water in kettle

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Constants
res = 50 #resolution



# Kettle parametrization 
def r(h, l): return (8-np.exp(h/14))*(1-l)
def x(theta, h, l): return r(h, l)*np.sin(theta);
def y(theta, h, l): return r(h, l)*np.cos(theta);
def z(h): return h;


# Figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection = "3d")

# Plotting
x_arr, y_arr, z_arr = [], [], []

for theta in np.linspace(0, 2*np.pi, res):
    for h in np.linspace(0,15,res):
        for l in np.linspace(0, 1, res//2):
            x_arr.append(x(theta, h, l))
            y_arr.append(y(theta, h, l))
            z_arr.append(z(h))
        
        
print("done")
ax.scatter3D(x_arr, y_arr, z_arr, color = "red")
print("done2")
plt.title("Kettle")
plt.axis("equal")
plt.show()