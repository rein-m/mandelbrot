import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mandelbrot(c, max_iterations):
    z = c
    for i in range(max_iterations):
        if abs(z) > 2.0:
            return i
        z = z * z + c
    return max_iterations

def create_mandelbrot_set(width, height, real_min, real_max, imag_min, imag_max, max_iterations):
    real_vals = np.linspace(real_min, real_max, width)
    imag_vals = np.linspace(imag_min, imag_max, height)
    mandelbrot_set = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = complex(real_vals[i], imag_vals[j])
            mandelbrot_set[i, j] = mandelbrot(c, max_iterations)

    return mandelbrot_set

# Set the parameters for the Mandelbrot set
width = 500
height = 500
real_min = -2.0
real_max = 1.0
imag_min = -1.5
imag_max = 1.5
max_iterations = 100

# Create the Mandelbrot set
mandelbrot_set = create_mandelbrot_set(width, height, real_min, real_max, imag_min, imag_max, max_iterations)

# Plot the Mandelbrot set in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.linspace(real_min, real_max, width), np.linspace(imag_min, imag_max, height))
ax.plot_surface(X, Y, mandelbrot_set, cmap='hot')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_zlabel('Iterations')

# Show the plot
plt.show()
