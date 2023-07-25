import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
σ = 10
ρ = 28
β = 8/3

# Function to compute the Lorenz system equations
def lorenz_system(x, y, z, σ, ρ, β):
    dx_dt = σ * (y - x)
    dy_dt = x * (ρ - z) - y
    dz_dt = x * y - β * z
    return dx_dt, dy_dt, dz_dt

# Time points
dt = 0.01
t = np.arange(0, 100, dt)

# Initial conditions
x_init = 1.0
y_init = 1.0
z_init = 1.0

# Arrays to store the solutions
x_values = [x_init]
y_values = [y_init]
z_values = [z_init]

# Numerical integration using Euler's method
for i in range(1, len(t)):
    dx, dy, dz = lorenz_system(x_values[-1], y_values[-1], z_values[-1], σ, ρ, β)
    x_values.append(x_values[-1] + dt * dx)
    y_values.append(y_values[-1] + dt * dy)
    z_values.append(z_values[-1] + dt * dz)

# Plotting the Lorenz attractor in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values, lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.show()
