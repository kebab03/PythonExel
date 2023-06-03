import numpy as np
import matplotlib.pyplot as plt

# Parameters
Lx = Ly = 1.0  # Domain size
nx = ny = 50  # Number of grid points
dx = Lx / (nx - 1)  # Grid spacing
dy = Ly / (ny - 1)
alpha = 1.0  # Thermal diffusivity
dt = dx**2 / (4 * alpha)  # Time step
nt = 1000  # Number of time steps

# Initial condition
T0 = np.zeros((nx, ny))
T0[nx // 4:3 * nx // 4, ny // 4:3 * ny // 4] = 1.0

# Boundary condition
Tleft = np.zeros(ny)
Tright = np.zeros(ny)
Ttop = np.zeros(nx)
Tbottom = np.zeros(nx)

# Main loop
T = T0.copy()
for n in range(nt):
    T[0, :] = Tbottom
    T[-1, :] = Ttop
    T[:, 0] = Tleft
    T[:, -1] = Tright
    T[1:-1, 1:-1] += alpha * dt * (
        (T[2:, 1:-1] - 2 * T[1:-1, 1:-1] + T[:-2, 1:-1]) / dx**2
        + (T[1:-1, 2:] - 2 * T[1:-1, 1:-1] + T[1:-1, :-2]) / dy**2
    )

# Plot the result
plt.imshow(T, cmap='hot', origin='lower', extent=[0, Lx, 0, Ly])
plt.colorbar()
plt.show()
