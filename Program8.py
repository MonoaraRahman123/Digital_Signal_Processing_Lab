#Perform circular convolution [Circle Method].
import numpy as np

# Step 1: Define input sequences
x = np.array([2, 1, 2, 1])
h = np.array([1, 2, 3, 4])

# Step 2: Find the sequence length
N = max(len(x), len(h))

# Step 3: Zero-pad both sequences to the same length
x = np.pad(x, (0, N - len(x)))
h = np.pad(h, (0, N - len(h)))

# Step 4: Create an output array
y = np.zeros(N)

# Step 5: Calculate circular convolution
for n in range(N):

    for k in range(N):
        y[n] += x[k] * h[(n - k) % N]

# Step 6: Display the final result
print("Input x[n]:", x)
print("Input h[n]:", h)
print("Circular Convolution:", y)