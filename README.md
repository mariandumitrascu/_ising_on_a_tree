# Find Ground States of an Ising Model on a Tree

This code is a script for finding the ground state of an Ising equation for a tree of nodes. It contains three functions:


`compute_ground_state(h, J)`: This function computes the ground state of the Ising equation using the D-Wave system. The input arguments are the dictionary of nodes weights h and the dictionary of edges weights J.

`read_input_file(filename)`: This function reads the input file and returns the Ising equation as dictionaries h and J. The input argument is the name of the input file.

`array_to_string(d)`: This function converts an array of 1 and -1 to a string of '+' and '-' characters. The input argument is an array of 1 and -1.

At the bottom of the code, `main()` function is defined, which calls the compute_ground_state and array_to_string functions to read the input file, compute the ground state, and energy of the Ising equation.

The `compute_ground_state` function first creates a list of possible spin values for a pair of nodes, i.e., (1, 1), (1, -1), (-1, 1), (-1, -1). It then creates an adjacency list for the graph defined by the Ising equation. The function compute_subtree is called with the root node and its parent to compute the energy and spin values for the subtree rooted at the node. This function recursively calls itself on the children of the node to compute the energy and spin values for their subtrees. The energy and spin values for the current node are computed for all possible spin values of the current node and the child node. The function then returns the partial energy and spin values for the current node. Finally, the function compute_ground_state computes the partial energy and spin values for the root subtree, finds the minimum energy and the corresponding spin value for the root node, and returns the minimum energy and spin value.


`compute_subtree(node, parent)` is a function that takes in two parameters, node and parent, which represent the current node and its parent node in a subtree of a graph. The purpose of this function is to compute the partial energy and spin values for the subtree rooted at the current node, recursively. The time complexity only by this function is O(n)

This function first initializes the energy and spin values for the current node, which are updated in the following steps. It then loops over the children of the current node and calls the compute_subtree function recursively on each child to compute their partial energy and spin values.

For each child, the energy and spin values are computed for all possible spin values of the current node and child node by looping over the parent_child_states list. For each pair of spin values, the energy and spin values for the current node are updated based on the energy and spin values of the child node, the energy of the edge between the current node and the child node, and the spin values of the current node and child node.

Since each child can be the root of a subtree, this function is called recursively on each child to compute the partial energy and spin values for their subtrees. This process continues until all the nodes in the subtree have been visited. Thus, this function is recursive as it calls itself with different node and parent parameters to compute the partial energy and spin values for all the nodes in the subtree rooted at the current node.

The script is using `sample_input.txt` as input data. To execute, create a conda environment, defined in `conda-env.yml`.

The script `test_on_a_tree.py` contains the unit tests for each of the function, using `pytest` package.
To test:

```bash

pytest test_on_a_tree.py

```
