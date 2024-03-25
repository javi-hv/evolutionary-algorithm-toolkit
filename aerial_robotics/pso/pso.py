import numpy as np
import matplotlib.pyplot as plt

# Objective function
def objective(a):
    return (a + 5) ** 2

# Random population generation
num_particles = 5
x = np.random.uniform(-100, 100, size=(num_particles, 1))
V = np.zeros_like(x)

miu = 0.01
max_iterations = 5
best_fitness = np.inf

# Plot the objective function
a = np.linspace(-100, 100, 400)
plt.plot(a, objective(a))
plt.xlabel('a')
plt.ylabel('y')
plt.title('Objective Function')

for k in range(max_iterations):
    # Evaluate fitness
    fitness = objective(x)
    best_index = np.argmin(fitness)
    best_fitness = fitness[best_index]

    # Update best position
    best_position = x[best_index]

    # Update velocity and position
    for i in range(num_particles):
        V[i] = miu * V[i] + (best_position - x[i])
        x[i] = miu * x[i] + V[i]

    # Plot
    plt.plot(x[:, 0], objective(x[:, 0]), 'o')
    plt.xlim([-100, 100])
    plt.ylim([-50, 10000])
    plt.pause(0.1)

plt.show()