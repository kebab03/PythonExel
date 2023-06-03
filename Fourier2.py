import numpy as np
import matplotlib.pyplot as plt

# Define the physical parameters
L = 1 # Length of the rod
T = 1 # Total time
kappa = 1 # Thermal diffusivity
N = 50 # Number of grid points
dx = L / (N - 1) # Grid spacing
dt = 0.001 # Time step

# Initialize the temperature array
u = np.zeros((N,))

# Set the initial and boundary conditions
u[0] = 0
u[N-1] = 0
u[1:N-1] = np.sin(np.pi * np.linspace(1, N-2, N-2))

# Define the finite difference matrix
A = np.zeros((N,N))
A[0,0] = 1
A[N-1,N-1] = 1
for i in range(1,N-1):
    A[i,i-1] = -kappa / dx**2
    A[i,i] = 2 * kappa / dx**2 + 1 / dt
    A[i,i+1] = -kappa / dx**2

# Solve the heat equation using finite differences
for n in range(int(T / dt)):
    b = np.zeros((N,))
    b[1:N-1] = u[1:N-1] / dt
    u = np.linalg.solve(A, b)

# Plot the temperature distribution
x = np.linspace(0, L, N)
plt.plot(x, u)
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.show()
