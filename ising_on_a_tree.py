import numpy as np


# ######################################################################################
def compute_ground_state(h, J):
    """
    Compute the ground state of the Ising equation using the D-Wave system.
    This is O(n log n) time complex algorithm and is useful for larger problems.

    Args:
        h (dict): dictionary with nodes weights, h[i] is the weight of node i, i=0,1,...,n-1, n is the number of nodes, h[i] is an integer
        J (dict): dictionary with edges weights, J[(i,j)] is the weight of edge (i,j), i,j=0,1,...,n-1, n is the number of nodes, J[(i,j)] is an integer
    """

    # Define the possible spin values for the parent and child nodes
    # We'll compute the energy and spin values for all possible spin values
    parent_child_states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Define the number of nodes
    n = len(h)

    # Create the adjacency list with n empty lists
    adj = [[] for _ in range(n)]

    # Loop over the edges and add the nodes to the adjacency list
    for (u, v) in J:
        adj[u].append(v)
        adj[v].append(u)

    # Define a function to compute the partial energy and spin values for a subtree
    def compute_subtree(node, parent):
        """ Takes a node and its parent as input and computes the energy and spin values for the subtree rooted at that node, recursively.

        Args:
            node (int): index of the node, node=0,1,...,n-1, n is the number of nodes
            parent (int): index of the parent node, parent=0,1,...,n-1, n is the number of nodes

        Returns:
            energy (dict): dictionary with the energy values for the subtree, energy[s] is the energy value for the subtree with spin s, s=1,-1
        """

        # Initialize the partial energy and spin values for the current node
        energy = {1: h[node], -1: -h[node]}
        # Initialize the spin values for the current node
        # spin[s] is the spin value for the current node with spin s, s=1,-1
        spin = {1: np.zeros(n), -1: np.zeros(n)}
        spin[1][node] = 1
        spin[-1][node] = -1

        # Loop over the children of the current node, cannot be so many
        for child in adj[node]:

            # Ignore the parent, we all do
            if child != parent:

                # Recursively compute the partial energy and spin values for the child subtree
                # We'll consider the subtree as one node, and we pass the current node as the parent
                child_spin, child_energy  = compute_subtree(child, node)

                # Loop over the possible spin values for the current node and the child node
                # Compute the energy and spin values for the current node and the child node, for the given spin values s, s=(s1,s2)
                # This is a loop over 4 values, so it's not so bad
                for s in parent_child_states:

                    # Unpack the spin values
                    s1, s2 = s

                    new_energy = {}
                    new_spin = {}

                    # Ising model energy definition,
                    # we add the energy of the child subtree, and the energy of the edge between the current node and the child node
                    new_energy[s1] = energy[s1] + child_energy[s2] + J[(node, child)] * s1 * s2

                    # Compute the new spin value for the current node,
                    # we add the spin value of the child node to the current node spin value
                    new_spin[s1] = spin[s1].copy() + child_spin[s2]

                    # Update the energy and spin values for the current node
                    # We only update the values if the new energy is lower than the current energy
                    if new_energy[s1] < energy[s1]:
                        energy[s1] = new_energy[s1]
                        spin[s1] = new_spin[s1]


        # Return the partial energy and spin values for the current node
        return spin, energy

    # Choose the root node, we'll use the first node
    root = 0

    # Compute the partial energy and spin values for the root subtree
    root_spin, root_energy  = compute_subtree(root, -1)

    # Find the minimum energy and the corresponding spin value for the root node
    min_energy = min(root_energy.values())
    # Find the index of the minimum energy value
    min_spin_ix = min(root_energy, key=root_energy.get)
    # Find the spin value for the root node with the minimum energy
    min_spin = root_spin[min_spin_ix]

    return min_spin, min_energy

# ######################################################################################
def read_input_file(filename):
    """
    Read the input file and return the Ising equation as h and J dictionaries.

    Args:
        filename (str): name of the input file
    """
    h = {}
    J = {}

    # read the input file and populate the h and J dictionaries with the weights of the nodes and edges of the Ising equation
    # h[i] is the weight of node i, i=0,1,...,n-1, n is the number of nodes, h[i] is an integer
    # J[(i,j)] is the weight of edge (i,j), i,j=0,1,...,n-1, n is the number of nodes, J[(i,j)] is an integer
    with open(filename, 'r') as f:
        for line in f:
            i, j, value = [int(x) for x in line.strip().split()]
            if i == j:
                h[i] = value
            else:
                J[(i, j)] = value
    return h, J

# ######################################################################################
def array_to_string(d):
    """
    Convert an array of 1 and -1 to a string of '+' and '-' characters.

    Args:
        d (array): array of 1 and -1
    """

    result = ''
    for i in d:
        if i == 1:
            result += '+'
        else:
            result += '-'
    return result

# ######################################################################################
def main():
    """
    Main function.
    """
    import os

    # get the path of this script
    script_path = os.path.dirname(os.path.realpath(__file__))
    # get the path of the input file
    file_path = os.path.join(script_path, 'sample_input.txt')

    # read the input file
    h, J = read_input_file(file_path)

    # compute the ground state, and the energy, of the Ising equation
    solution, energy  = compute_ground_state(h, J)

    # convert to ++++---++
    solution_spins = array_to_string(solution)

    print(energy)
    print(solution_spins)


# ######################################################################################
# ######################################################################################
# ######################################## MAIN ########################################
if __name__ == '__main__':

    main()

