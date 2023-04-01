import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# Define a function
def func(x):
    return (x[0]-1)**2 + (x[1]-6)**2

# Find the minimum using the BFGS method
M = minimize(func, [0, 0], method='BFGS')

# Create a 3D plot 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.linspace(-6, 6, 50), np.linspace(-6, 6, 50))
Z = func([X, Y])

ax.plot_surface(X, Y, Z, cmap='viridis')

# Plot the minimum point
ax.scatter(M.x[0], M.x[1], M.fun, color='black', s=100)
plt.show()
print("Minimum value: ", M.fun)


