import numpy as np
from pyswarm import pso
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the objective (to be minimized)
def weight(x, *args):
    H, d, t = x
    B, rho, E, P = args
    return rho * np.pi * d * t * np.sqrt((B/2)**2 + H**2)

# Setup the constraint functions
def yield_stress(x, *args):
    H, d, t = x
    B, rho, E, P = args
    return (P * np.sqrt((B/2)**2 + H**2)) / (2 * t * np.pi * d * H)

def buckling_stress(x, *args):
    H, d, t = x
    B, rho, E, P = args
    return (np.pi**2 * E * (d**2 + t**2)) / (8 * ((B/2)**2 + H**2))

def deflection(x, *args):(optimizatio)**2 + H**2)**3) / (2 * t * np.pi * d * H**2 * E)

def constraints(x, *args):
    strs = yield_stress(x, *args)
    buck = buckling_stress(x, *args)
    defl = deflection(x, *args)
    return [1000000 - strs, buck - strs, 0.00635 - defl]  # Converting kpsi to psi, and in to meters

# Define the other parameters
B = 1.524  # meters (60 inches)
rho = 4810  # kg/m^3 (0.3 lb/in^3)
E = 20684300000  # Pa (30000 kpsi)
P = 294.3  # kN (66 kip, 1 kip = 4.448 kN)
args = (B, rho, E, P)

# Define the lower and upper bounds for H, d, t, respectively
lb = [0.254, 0.0254, 0.000254]  # meters (10 inches, 1 inch, 0.01 inch)
ub = [0.762, 0.0762, 0.00635]  # meters (30 inches, 3 inches, 0.25 inch)

# Optimize with PSO
xopt, fopt = pso(weight, lb, ub, f_ieqcons=constraints, args=args)

# Print optimal values
print("Optimal values:")
print("H: {:.2f} m, d: {:.2f} m, t: {:.5f} m".format(xopt[0], xopt[1], xopt[2]))
print("Weight: {:.2f} kg".format(fopt))

# Plot the A-frame truss in 3D
H, d, t = xopt

# Define coordinates for the truss
node_coords = np.array([[0, 0, 0], [d/2, 0, -H], [-d/2, 0, -H]])

# Connect the nodes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(node_coords)):
    ax.scatter(node_coords[i, 0], node_coords[i, 1], node_coords[i, 2], color='b')
for i in range(len(node_coords)):
    for j in range(i+1, len(node_coords)):
        ax.plot([node_coords[i, 0], node_coords[j, 0]], [node_coords[i, 1], node_coords[j, 1]],
                [node_coords[i, 2], node_coords[j, 2]], color='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('A-frame Truss Design')

plt.show()
