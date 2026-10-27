#Convert continuous time signal to discrete time signal.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
f_signal = 4.0      # Frequency of analog signal in Hz
fs = 40.0           # Sampling rate in Hz (fs >= 2 * f_signal)
duration = 1.0

# 1. Analog (Continuous) approximation using dense points
t_analog = np.linspace(0, duration, 1000)
x_analog = np.sin(2 * np.pi * f_signal * t_analog)

# 2. Discrete Sampling  
n = np.arange(0, int(fs * duration))
t_samples = n / fs
x_discrete = np.sin(2 * np.pi * f_signal * t_samples)

# Plotting
plt.figure(figsize=(9, 4))
plt.plot(t_analog, x_analog, 'b-', label='Analog $x(t) = \sin(2\pi \cdot 4 t)$')
plt.stem(t_samples, x_discrete, linefmt='r-', markerfmt='ro', basefmt='k--', label='Sampled $x[n]$')
plt.title('Problem 01: Sampling Continuous Signal to Discrete Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()