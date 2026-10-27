#Perform convolution operation.
import numpy as np

# Step 1: Define input signals
x = np.array([1, 2, 3, 4])
h = np.array([1, 1, 1])

# Step 2: Find signal lengths
L = len(x)
M = len(h)

# Step 3: Find output length
N = L + M - 1

# Step 4: Create output array
y = np.zeros(N)

# Step 5: Calculate convolution
for n in range(N):
    for k in range(L):
        if 0 <= n-k < M:
            y[n] += x[k] * h[n-k]

# Step 6: Show the results
print("Input x[n]:", x)
print("Input h[n]:", h)
print("Linear Convolution:", y)

# Step 7: Verify the result
print("NumPy Result:", np.convolve(x, h))