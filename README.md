# Find Ground States of an Ising Model on a Tree

This code is a script for finding the ground state of an Ising equation for a tree of nodes.


compute_subtree(node, parent) is a function that takes in two parameters, node and parent, which represent the current node and its parent node in a subtree of a graph. The purpose of this function is to compute the partial energy and spin values for the subtree rooted at the current node, recursively.

This function first initializes the energy and spin values for the current node, which are updated in the following steps. It then loops over the children of the current node and calls the compute_subtree function recursively on each child to compute their partial energy and spin values.

For each child, the energy and spin values are computed for all possible spin values of the current node and child node by looping over the parent_child_states list. For each pair of spin values, the energy and spin values for the current node are updated based on the energy and spin values of the child node, the energy of the edge between the current node and the child node, and the spin values of the current node and child node.

Since each child can be the root of a subtree, this function is called recursively on each child to compute the partial energy and spin values for their subtrees. This process continues until all the nodes in the subtree have been visited. Thus, this function is recursive as it calls itself with different node and parent parameters to compute the partial energy and spin values for all the nodes in the subtree rooted at the current node.

The script is using `sample_input.txt` as input data. To execute, create a conda environment, defined in `conda-env.yml`.

The script `test_on_a_tree.py` contains the unit tests for each of the function, using `pytest` package.
To test:

```bash

pytest test_on_a_tree.py

```
