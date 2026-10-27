#Perform addition operation of signals.
import numpy as np
import matplotlib.pyplot as plt

# Define two signals with different index supports
n1 = np.arange(-3, 4)
x1 = np.array([1, 2, 3, 4, 3, 2, 1])
n2 = np.arange(0, 7)
x2 = np.array([2, -1, 3, 0, 1, 4, -2])
   
# Find the union of time intervals
n_min = min(n1[0], n2[0])
n_max = max(n1[-1], n2[-1])
n_total = np.arange(n_min, n_max + 1)

# Align signals on the unified time base with zero-padding
y1 = np.zeros(len(n_total))
y2 = np.zeros(len(n_total))

y1[(n_total >= n1[0]) & (n_total <= n1[-1])] = x1
y2[(n_total >= n2[0]) & (n_total <= n2[-1])] = x2

# Element-wise addition
y_add = y1 + y2

plt.figure(figsize=(8, 7))
plt.subplot(3, 1, 1)
plt.stem(n_total, y1, basefmt='k--')
plt.title('Signal $x_1[n]$ (Aligned)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n_total, y2, basefmt='k--')
plt.title('Signal $x_2[n]$ (Aligned)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n_total, y_add, basefmt='k--')
plt.title('Addition Output: $y[n] = x_1[n] + x_2[n]$')
plt.grid(True)

plt.tight_layout()
plt.show()