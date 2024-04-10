import numpy as np
import matplotlib.pyplot as plt

# Objective function
def Objective(a):
    return (a+5)**2+10*np.sin(a)

# Custom learning rate calculation function
def custom_learning_rate(x_k, x_km1, grad_k, grad_km1):
    step = np.abs(((np.transpose(x_k - x_km1)* (grad_k - grad_km1)))/((grad_k - grad_km1)**2))
    return step

# Plot
a_values = np.linspace(-15, 4, 400)
plt.plot(a_values, Objective(a_values), label='Objective Function')
plt.xlabel('a')
plt.ylabel('Objective Function Value')
plt.title('Gradient Descent Optimization')
plt.grid(True)
plt.legend()

# Initialization
x = [2]  # random parameter
tol = 0.001  # epsilon
error = 1
h = 0.01  # h of numerical derivate calculation
step = 0.05  # t_k
k = 0  # count

# Gradient Descent
while error > tol:
    grad = (Objective(x[k]) - Objective(x[k] - h)) / h
    x.append(x[k] - step * grad)
    error = abs(x[k + 1] - x[k])  # to stop algorithm
    k += 1

    # Plot
    plt.plot(x[k], Objective(x[k]), 'ro')
    plt.xlim(-15, 4)
    plt.ylim(-50, 230)
    plt.pause(0.1)

plt.show()

# Plot
a_values = np.linspace(-15, 4, 400)
plt.plot(a_values, Objective(a_values), label='Objective Function')
plt.xlabel('a')
plt.ylabel('Objective Function Value')
plt.title('Gradient Descent Optimization')
plt.grid(True)
plt.legend()

# Initialization
x = [2]  # random parameter
tol = 0.001  # epsilon
error = 1
h = 0.01  # h of numerical derivate calculation
step = 0.05  # t_k
k = 0  # count
grad_prev = 0
 
# Gradient Descent with change step
while error > tol:
    grad = (Objective(x[k]) - Objective(x[k] - h)) / h
    if k > 0.5:
        learning_rate = custom_learning_rate(x[k], x[k-1], grad, grad_prev)
    else:
        learning_rate = step
    
    x.append(x[k] - learning_rate * grad)
    grad_prev = grad
    error = abs(x[k + 1] - x[k])  # to stop algorithm
    k += 1
 
    # Plot
    plt.plot(x[k], Objective(x[k]), 'g x')
    plt.xlim(-15, 4)
    plt.ylim(-50, 230)
    plt.pause(0.1)
 
plt.show()
