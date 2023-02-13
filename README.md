# Find Ground States of an Ising Model on a Tree

This code is a script for finding the ground state of an Ising equation using different optimization algorithms.

The code defines several functions for computing the ground state of an Ising equation:

`compute_ground_state`: Computes the ground state of the Ising equation using the D-Wave system. This function converts the Ising equation into a binary quadratic model (BQM) using dimod library, and solves the BQM using the EmbeddingComposite class of the dwave.system library, which is a composite of a number of samplers, including the DWaveSampler.

`compute_ground_state_exactsolver`: Computes the ground state of the Ising equation using the ExactSolver, which is an exact solution method for small problems and is provided by the dimod library.

`compute_ground_state_hybridsampler`: Computes the ground state of the Ising equation using the LeapHybridSampler from the dwave.system library.

`compute_ground_state_simulated_annealing`: Computes the ground state of the Ising equation using simulated annealing, a classic optimization algorithm.

The `read_input_file` function reads an input file in the form of an Ising equation and converts it into dictionaries h and J representing the Ising equation.

The `dict_to_string` function converts a dictionary into a string of '+' and '-' characters.

Finally, the main function reads the input file and calls the compute_ground_state function to find the ground state solution and energy of the Ising equation. The solution is then printed in the form of a string of '+' and '-' characters, and the energy is also printed.

The script is using `sample_input.txt` as input data. To execute, create a conda environment, defined in `conda-env.yml`. 

The script `test_on_a_tree.py` contains the unit tests for each of the function, using `pytest` package.
To test:

```bash

pytest test_on_a_tree.py

```
