# Numerical Integration Methods Visualization

This Python script demonstrates the visualization of three numerical integration methods: Simpson's Rule, Trapezoidal Rule, and Left Rectangle Method. It also compares their accuracy in approximating the area under a challenging integrand function.

## Prerequisites
- Python 3.9
- Required Python libraries: numpy, matplotlib, scipy

## Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required Python libraries using pip:
    ```
    pip install numpy matplotlib scipy
    ```

## Usage
1. Open the Python script `numerical_integration_visualization.py`.
2. Modify the integration bounds (`a` and `b`) and the number of intervals (`n`) as needed.
3. Run the script.

## Description
- `challenging_integrand(x)`: Defines the challenging integrand function `sin(10*x)`.
- `simpson_visual(f, a, b, n)`: Visualizes Simpson's Rule approximation for the integral of the defined function.
- `left_rectangle_visual(f, a, b, n)`: Visualizes the Left Rectangle Method approximation for the integral of the defined function.
- `trapezoidal_visual(f, a, b, n)`: Visualizes the Trapezoidal Rule approximation for the integral of the defined function.
- `a`, `b`: Integration bounds.
- `n`: Number of intervals for approximation.

## Results
After running the script, it will display visualizations of each numerical integration method's approximation for the integral of the defined function. Additionally, it will print the approximated area using each method and the actual area computed using scipy's `quad` function, along with their accuracies.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
