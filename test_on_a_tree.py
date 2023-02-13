import os
import numpy as np
import random
from ising_on_a_tree_dwave import *
import pytest

def test_compute_ground_state():
    # Test input
    h = {0: -1, 1: -1, 2: -1, 3: -1}
    J = {(0, 1): 1, (1, 2): 1, (1, 3): 1}

    # Call the function to get the output
    solution, energy = compute_ground_state(h, J)
    solution_actual, energy_actual = compute_ground_state_exactsolver(h, J)

    # Assert that the output is as expected
    assert solution == solution_actual, f"Expected {solution_actual}, but got {solution}"
    assert energy == energy_actual, f"Expected {energy_actual}, but got {energy}"

def test_compute_ground_state_exactsolver():
    # Test input
    h = {0: -1, 1: -1, 2: -1, 3: -1}
    J = {(0, 1): 1, (1, 2): 1, (1, 3): 1}

    # Call the function to get the output
    solution, energy = compute_ground_state_exactsolver(h, J)

    # Assert that the output is as expected
    assert isinstance(solution, dict)
    assert isinstance(energy, float)

def test_compute_ground_state_hybridsampler():
    # Test input
    h = {0: -1, 1: -1, 2: -1, 3: -1}
    J = {(0, 1): 1, (1, 2): 1, (1, 3): 1}

    # Call the function to get the output
    solution, energy = compute_ground_state_hybridsampler(h, J)

    # Assert that the output is as expected
    assert isinstance(solution, dict)
    assert isinstance(energy, float)

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

def test_dict_to_string():
    # Test input
    d = {0: 1, 1: -1, 2: -1, 3: 1}

    # Call the function to get the output
    result = dict_to_string(d)

    # Assert that the output is as expected
    assert isinstance(result, str)
    assert result == '+--+'
