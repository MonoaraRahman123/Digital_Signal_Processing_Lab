#Perform circular covolution [Matrix Method].
import numpy as np

# Step 1: Define input sequences
x = np.array([1, 2, 3, 4])
h = np.array([2, 1, 2, 1])

# Step 2: Find the sequence length
N = max(len(x), len(h))

# Step 3: Zero-pad both sequences to the same length
x = np.pad(x, (0, N - len(x)))
h = np.pad(h, (0, N - len(h)))

# Step 4: Construct the circulant matrix H
H = np.zeros((N, N))

for n in range(N):
    for k in range(N):
        H[n, k] = h[(n - k) % N]

# Step 5: Perform matrix-vector multiplication
y = np.dot(H, x)

# Step 6: Display the results
print("\nConstructed Circular Matrix H:\n", H)
print("\nOutput Vector y = H * x:\n", y)
