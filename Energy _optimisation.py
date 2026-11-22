import numpy as np
import matplotlib.pyplot as plt

# Objective function after variable elimination
# f(x1) = 2(x1 - 80)^2
def f(x1):
    return 2 * (x1 - 80)**2

# Generate x1 values for plotting
x1 = np.linspace(0, 100, 500)

# Compute objective function values
y = f(x1)

# Optimal solution obtained analytically
x1_opt = 80
x2_opt = 20

# Minimum objective function value
f_opt = f(x1_opt)

# Plot the objective function
plt.figure(figsize=(8,5))
plt.plot(x1, y, label='Objective Function')

# Plot the optimal point
plt.scatter(x1_opt, f_opt, label='Optimal Solution')

# Labels and title
plt.xlabel('x1')
plt.ylabel('f(x1)')
plt.title('Optimization Result')

# Display legend and grid
plt.legend()
plt.grid(True)

# Print optimal results
print("Optimal Solution:")
print("x1 =", x1_opt)
print("x2 =", x2_opt)
print("Minimum Objective Function Value =", f_opt)

# Show plot
plt.show()