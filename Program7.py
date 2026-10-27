#Perform deconvolution operation.
import numpy as np

# Step 1: Define the observed output and system response
y = np.array([1, 3, 6, 9, 7, 4], dtype=float)
h = np.array([1, 1, 1])

# Step 2: Find signal lengths
L = len(y)
M = len(h)

# Step 3: Find the recovered input length
N = L - M + 1

# Step 4: Create the input array
x = np.zeros(N)

# Step 5: Recover the input using manual deconvolution
for n in range(N):
    curr_sum = 0

    for k in range(1, min(n + 1, M)):
        curr_sum += h[k] * x[n - k]

    x[n] = (y[n] - curr_sum) / h[0]

# Step 6: Display the results
print("Observed Output y[n]:", y)
print("System Response h[n]:", h)
print("Recovered Input x[n]:", x)