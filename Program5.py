#Find even and odd components of a signal.
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Sample index
n = np.arange(-5, 6)

# Step 2: Original signal
x = np.array([0, 0, 1, 3, 5, 4, 2, 1, 0, 0, 0], dtype=float)

# Step 3: Reverse the signal
x_reversed = x[::-1]

# Step 4: Find even signal
x_even = 0.5 * (x + x_reversed)

# Step 5: Find odd signal
x_odd = 0.5 * (x - x_reversed)

# Step 6: Plot original signal
plt.figure(figsize=(9, 7))

plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt='k--')
plt.title('Original Signal x[n]')
plt.grid(True)

# Step 7: Plot even signal
plt.subplot(3, 1, 2)
plt.stem(n, x_even, basefmt='k--')
plt.title('Even Signal')
plt.grid(True)

# Step 8: Plot odd signal
plt.subplot(3, 1, 3)
plt.stem(n, x_odd, basefmt='k--')
plt.title('Odd Signal')
plt.grid(True)

# Step 9: Show the graphs
plt.tight_layout()
plt.show()