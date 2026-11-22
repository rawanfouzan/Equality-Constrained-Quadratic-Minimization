# Equality-Constrained Quadratic Minimization

A Python-based course project for solving an equality-constrained quadratic optimization problem using the **Variable Elimination Method**.

## Project Overview

This project focuses on optimizing energy allocation between solar energy and grid electricity while satisfying a required total energy demand.

The objective is to minimize the deviation from a desired energy allocation.

## Mathematical Formulation

**Objective Function:**

\[
f(x) = (x_1 - 80)^2 + (x_2 - 20)^2
\]

**Equality Constraint:**

\[
x_1 + x_2 = 100
\]

Where:
- \(x_1\): Amount of solar energy.
- \(x_2\): Amount of grid electricity.

## Methodology

The problem is solved using the Variable Elimination Method:

1. Express \(x_2\) in terms of \(x_1\).
2. Substitute the equality constraint into the objective function.
3. Reduce the problem to a single-variable unconstrained minimization problem.
4. Determine the optimal solution analytically.
5. Visualize the objective function using Python.

## Results

The optimal solution is:

| Variable | Optimal Value |
|---|---:|
| Solar Energy (x1) | 80 |
| Grid Electricity (x2) | 20 |
| Minimum Objective Value | 0 |

## Visualizations

The project includes a graphical representation of the objective function and its optimal solution.

## Technologies Used

- Python
- NumPy
- Matplotlib

## Project Structure

```text
Equality-Constrained-Quadratic-Minimization/
│
├── Energy_optimisation.py
├── Report.pdf
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install the required libraries:

```bash
pip install numpy matplotlib
```

3. Run the Python script:

```bash
python Energy_optimisation.py
```

## Course Information

**Course:** Applied Optimization: Formulation and Algorithms

**Project Topic:** Equality-Constrained Quadratic Optimization

**Method:** Variable Elimination (Direct Analytical Method)

**Language:** Python
