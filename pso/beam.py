import numpy as np
from pyswarm import pso
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Objective Function: Weight of the beam (to be minimized)
def weight(area):
    density_steel = 7850  # kg/m^3
    length = 5  # meters (Length of the beam)
    return area * length * density_steel

# Constraint 2: Deflection (must be less than a specified limit)
def deflection(area):
    modulus_of_elasticity = 200e9  # Pa (Young's modulus of steel)
    moment_of_inertia = area ** 2 / 12  # Moment of inertia for rectangular cross-section
    length = 5  # meters (Length of the beam)
    point_load = 1000  # N (Point load at the tip of the beam)
    return (point_load * length ** 3) / (3 * modulus_of_elasticity * moment_of_inertia)

# Constraint 3: Stress constraint (yield stress)
def stress_constraint(area):
    yield_stress = 250e6  # Pa (Yield stress of steel)
    return yield_stress - bending_stress(area)

# Constraint 1: Stress due to bending (must be less than yield stress)
def bending_stress(area):
    modulus_of_elasticity = 200e9  # Pa (Young's modulus of steel)
    moment_of_inertia = area ** 2 / 12  # Moment of inertia for rectangular cross-section
    distance_from_neutral_axis = area / 2  # Distance from neutral axis to the farthest fiber
    point_load = 1000  # N (Point load at the tip of the beam)
    length = 5  # meters (Length of the beam)
    return (point_load * length * distance_from_neutral_axis) / (moment_of_inertia * modulus_of_elasticity)

# Constraint: Combined stress constraint and deflection constraint
def constraints(area):
    stress = stress_constraint(area)
    defl = deflection(area)
    return [stress, defl]

# Define lower and upper bounds for the cross-sectional area
lb = [0.001]  # m^2 (Lower bound)
ub = [0.1]  # m^2 (Upper bound)

# Optimization with PSO
optimal_area, _ = pso(weight, lb, ub, f_ieqcons=constraints)

# Printing the results
print("Optimized Cross-sectional Area: {:.6f} m^2".format(optimal_area[0]))
print("Minimum Weight of the Beam: {:.6f} kg".format(weight(optimal_area[0])))

# Plotting the cantilever beam in 3D with cross-section
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Define the coordinates for plotting the beam
x_beam = np.array([0, 5])
y_beam = np.array([0, 0])
z_beam = np.array([0, 0])

# Plot the beam
ax.plot(x_beam, y_beam, z_beam, color='k', linewidth=2)

# Plot the point load at the tip
ax.scatter([5], [0], [0], color='r', s=100)

# Plot the cross-section of the beam
cross_section_length = 0.2  # Length of the cross-section
cross_section_height = 0.1  # Height of the cross-section
cross_section_width = optimal_area[0] / cross_section_length  # Width of the cross-section

# Define coordinates of the rectangular prism representing the cross-section
x_cross_section = np.array([[0, cross_section_length, cross_section_length, 0, 0],
                            [0, cross_section_length, cross_section_length, 0, 0]])
y_cross_section = np.array([[cross_section_height, cross_section_height, cross_section_height, cross_section_height, cross_section_height],
                            [0, 0, 0, 0, 0]])
z_cross_section = np.array([[0, 0, cross_section_width, cross_section_width, 0],
                            [0, 0, cross_section_width, cross_section_width, 0]])

# Translate the cross-section to the tip of the beam
x_cross_section += 5  # Move to the end of the beam

# Plot the cross-section
ax.plot_surface(x_cross_section, y_cross_section, z_cross_section, alpha=0.5)

# Set labels and title
ax.set_xlabel('Length (m)')
ax.set_ylabel('Height (m)')
ax.set_zlabel('Width (m)')
ax.set_title('Cantilever Beam with Point Load at the Tip and Cross-section')

plt.show()