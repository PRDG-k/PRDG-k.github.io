import numpy as np
import matplotlib.pyplot as plt

# N range
N = np.arange(1, 201)

# Algorithm A: constant time (horizontal line at 10000)
A = 10000 * np.ones_like(N)

# Algorithm B: polynomial time (quadratic growth)
B = N ** 2.2

# Plot
plt.figure(figsize=(8, 6))
plt.plot(N, A, 'k--', label='Algorithm A')   # dashed line
plt.plot(N, B, 'k.', label='Algorithm B')    # dotted points

# Threshold where B exceeds A
threshold_index = np.argmax(B > A[0])
plt.axvline(x=N[threshold_index], color='gold', linestyle='--', linewidth=2)

# Labels and legend
plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time')
plt.legend()

# Set y-axis limit to match the original graph
plt.ylim(0, 80000)

# Title
plt.title('Figure 4.3: Polynomial vs Sub-linear Time Algorithm')

plt.tight_layout()
plt.show()
