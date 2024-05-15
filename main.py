import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the challenging integrand function
def challenging_integrand(x):
    return np.sin(10 * x)

# Simpson's Rule implementation for visualization
def simpson_visual(f, a, b, n):
    if n % 2:  # n must be even for Simpson's rule
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Compute Simpson's Rule
    area_approx = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))

    # Plotting
    X = np.linspace(a, b, 1000)
    Y = f(X)

    plt.figure(figsize=(10, 6))
    plt.plot(X, Y, 'r', linewidth=2, label='Integrand')
    plt.plot(x, y, 'bo')

    for i in range(0, n, 2):
        xx = np.linspace(x[i], x[i + 2], 100)
        p = np.polyfit([x[i], x[i + 1], x[i + 2]], [y[i], y[i + 1], y[i + 2]], 2)
        yy = np.polyval(p, xx)
        plt.plot(xx, yy, 'g')
        plt.fill_between(xx, 0, yy, color='green', alpha=0.3)

    plt.title("Simpson's Rule Approximation for $\int_{0}^{0.9\pi} \sin(10x) dx$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return area_approx
def left_rectangle_visual(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b - h, n)  # Left end points
    y = f(x)

    # Compute Left Rectangle Method
    area_approx = h * np.sum(y)

    # Plotting
    X = np.linspace(a, b, 1000)
    Y = f(X)

    plt.figure(figsize=(10, 6))
    plt.plot(X, Y, 'r', linewidth=2, label='Integrand')

    for i in range(n):
        plt.bar(x[i], y[i], width=h, color='green', edgecolor='black', alpha=0.3, align='edge')

    plt.title("Left Rectangle Approximation for $\int_{0}^{0.9\pi} \sin(10x) dx$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return area_approx


def trapezoidal_visual(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # End points
    y = f(x)

    # Compute Trapezoidal Method
    area_approx = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

    # Plotting
    X = np.linspace(a, b, 1000)
    Y = f(X)

    plt.figure(figsize=(10, 6))
    plt.plot(X, Y, 'r', linewidth=2, label='Integrand')

    for i in range(n):
        plt.fill_between([x[i], x[i + 1]], [y[i], y[i + 1]], color='green', alpha=0.3)
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], 'g')

    plt.title("Trapezoidal Approximation for $\int_{0}^{0.9\pi} \sin(10x) dx$")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return area_approx
# Integration bounds and number of intervals
a, b = 0, 0.9 * np.pi
n = 100  # Number of intervals (even number for proper Simpson's Rule application)

# Calculate the approximate area using Simpson's Rule
approx_area = simpson_visual(challenging_integrand, a, b, n)
approx_area3 = trapezoidal_visual(challenging_integrand, a, b, n)
approx_area2 = left_rectangle_visual(challenging_integrand, a, b, n)
actual_area, _ = quad(challenging_integrand, a, b)

# Calculate the actual area using scipy's quad function
print(f"Approximated Area using Left Rectangle Method: {approx_area2}")
print(f"Approximated Area using Trapezoidal Method: {approx_area3}")
print(f"Approximated Area using Simpsons method: {approx_area}")
print(f"Actual Area: {actual_area}")
print(f"Accuracy using Left Rectangle Method: {actual_area-approx_area2}")
print(f"Accuracy using Trapezoidal method: {actual_area-approx_area3}")
print(f"Accuracy using Simpsons method: {actual_area-approx_area}")


