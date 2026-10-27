#Perform amplitude scaling of signals.
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Sample index
n = np.arange(-4, 5)

# Step 2: Original signal
x = np.array([0, 1, 2, 3, 2, 1, 0, -1, -2])

# Step 3: Scaling value
alpha = 2.5

# Step 4: Multiply the signal
y = alpha * x

# Step 5: Plot the original signal
plt.figure(figsize=(9, 4))
plt.stem(n-0.05 , x, linefmt='b-', markerfmt='bo', basefmt='k--', label='Original x[n]')

# Step 6: Plot the scaled signal
plt.stem(n, y, linefmt='r-', markerfmt='ro', basefmt='k--', label='Scaled y[n]')

# Step 7: Add title and labels
plt.title('Amplitude Scaling')
plt.xlabel('Sample Index n')
plt.ylabel('Amplitude')

# Step 8: Show the graph
plt.legend()
plt.grid(True)
plt.show()