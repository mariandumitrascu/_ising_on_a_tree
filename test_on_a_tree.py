import math
import os
import random

import numpy as np
import pytest
from ising_on_a_tree import *


# ######################################################################################
def compute_ground_state_exactsolver(h, J):
    """
    Compute the ground state of the Ising equation using the ExactSolver.
    This is an O(2^n) algorithm and is only useful for small problems.
    This can be used to verify the results of the other algorithms.
    """

    # Import the ExactSolver here so it wont show on top of the file
    import dimod

    # Create a binary quadratic model (BQM) from the Ising equation
    bqm = dimod.BinaryQuadraticModel.from_ising(h, J)

    # Use the ExactSolver to solve the BQM
    solver = dimod.ExactSolver()
    sampleset = solver.sample(bqm)

    # Extract the sample with the lowest energy
    solution = sampleset.first.sample

    # Calculate the energy of the sample with the lowest energy
    energy = sampleset.first.energy

    return solution, energy

# ######################################################################################
def test_compute_ground_state():
    # Test input
    h = {0: -1, 1: -1, 2: -1, 3: -1}
    J = {(0, 1): 1, (1, 2): 1, (1, 3): 1}

    # Call the function to get the output
    solution, energy = compute_ground_state(h, J)
    solution_actual, energy_actual = compute_ground_state_exactsolver(h, J)
    solution_actual = np.array(list(solution_actual.values()))

    print('solution', solution)
    print('solution_actual', solution_actual)

    # Assert that the output is as expected
    assert solution.all() == solution_actual.all(), f"Expected {solution_actual}, but got {solution}"
    assert energy == energy_actual, f"Expected {energy_actual}, but got {energy}"

def test_read_input_file():
    # Test input
    filename = 'test_input.txt'

    # Write the test file
    with open(filename, 'w') as f:
        f.write('0 0 1\n')
        f.write('1 1 -1\n')
        f.write('2 3 1\n')

    # Call the function to get the output
    h, J = read_input_file(filename)

    # Assert that the output is as expected
    assert isinstance(h, dict)
    assert isinstance(J, dict)
    assert h == {0: 1, 1: -1}
    assert J == {(2, 3): 1}

    # Remove the test file
    os.remove(filename)

def test_array_to_string():

    # Test input
    d = [1, -1, -1, 1]

    # Call the function to get the output
    result = array_to_string(d)

    # Assert that the output is as expected
    assert isinstance(result, str)
    assert result == '+--+'
