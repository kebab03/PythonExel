import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 0.8  # thermal conductivity
A = 1  # cross-sectional area
L = 1  # length of the wall
dx = 0.01  # spatial step
dt = 0.01  # time step
t_end = 10  # end time

# Grid
x = np.arange(0, L+dx, dx)
t = np.arange(0, t_end+dt, dt)
nt = len(t)
nx = len(x)

# Initial conditions
T0 = 0  # initial temperature
T = T0*np.ones(nx)
T[0] = 100  # temperature at left boundary

# Solve
Q = np.zeros(nx)
for i in range(1, nt):
    dTdx = (T[1:] - T[:-1])/dx
    Q[1:-1] = k*A*dTdx[1:]
    T[1:-1] += dt*(Q[:-2] - Q[1:-1])/A/k/dx
    T[0] = 100  # temperature at left boundary
    T[-1] = 0  # temperature at right boundary

# Plot results
plt.plot(x, T)
plt.xlabel('Position (m)')
plt.ylabel('Temperature (C)')
plt.show()
