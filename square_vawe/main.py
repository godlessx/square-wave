import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y = np.zeros(len(x))

for n in range(1, 26, 2):
    y += (4 / np.pi) * np.sin(n * x) / n

plt.plot(x, y, label="Square Wave Approximation")

plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")
plt.title("Square Wave Approximation (25 Harmonics)")

plt.grid()
plt.legend()
plt.show()