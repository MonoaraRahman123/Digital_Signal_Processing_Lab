#Perform multiplication operation of signals.
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 30)

# Carrier signal and modulating envelope
x1 = np.cos(0.4 * np.pi * n)       # Carrier
x2 = 0.85 ** n                     # Decaying exponential envelope

# Pointwise multiplication
y_mul = x1 * x2

plt.figure(figsize=(8, 7))
plt.subplot(3, 1, 1)
plt.stem(n, x1, basefmt='k--')
plt.title('Signal $x_1[n] = \cos(0.4\pi n)$')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, x2, basefmt='k--')
plt.title('Signal $x_2[n] = (0.85)^n$')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y_mul, basefmt='k--')
plt.title('Multiplication Output: $y[n] = x_1[n] \cdot x_2[n]$')
plt.grid(True)

plt.tight_layout()
plt.show()