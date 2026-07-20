"""
KVL Mesh Equation Solver
Author: Prarthana Holambe 

Description:
This program solves mesh currents using Kirchhoff's Voltage Law (KVL)
by representing the equations as a matrix and solving them with NumPy.
"""

import numpy as np


def get_matrix(n):
    """Read coefficient matrix from the user."""
    matrix = []

    print("\nEnter the coefficients for each equation:\n")

    for i in range(n):
        row = list(map(float, input(f"Equation {i+1}: ").split()))

        while len(row) != n:
            print(f"Please enter exactly {n} coefficients.")
            row = list(map(float, input(f"Equation {i+1}: ").split()))

        matrix.append(row)

    return np.array(matrix)


def get_constants(n):
    """Read constant values (RHS)."""
    constants = []

    print("\nEnter the RHS values:")

    for i in range(n):
        value = float(input(f"Equation {i+1}: "))
        constants.append(value)

    return np.array(constants)


def solve_kvl(A, B):
    """Solve the system of linear equations."""

    try:
        currents = np.linalg.solve(A, B)
        return currents

    except np.linalg.LinAlgError:
        return None


def display_result(currents):

    if currents is None:
        print("\nNo unique solution exists.")
        return

    print("\n========== RESULTS ==========")

    for i, current in enumerate(currents):
        print(f"I{i+1} = {current:.4f} A")


def main():

    print("=" * 40)
    print("     KVL MESH ANALYSIS SOLVER")
    print("=" * 40)

    n = int(input("\nEnter number of mesh currents: "))

    A = get_matrix(n)
    B = get_constants(n)

    currents = solve_kvl(A, B)

    display_result(currents)


if __name__ == "__main__":
    main()
