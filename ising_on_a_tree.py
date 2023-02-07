import os
import numpy as np
from scipy.linalg import eigh

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, 'input.txt')


def compute_transfer_matrix(tree, weights, J, num_spins):
    """Compute the transfer matrix for an Ising spin model on a tree with edge weights and different interaction strengths"""
    matrix = np.zeros((2 * num_spins, 2 * num_spins))
    for i, j in tree:
        matrix[i, i + num_spins] = 1
        matrix[j, j + num_spins] = 1
        matrix[i, j] = J
        matrix[i + num_spins, j + num_spins] = -J
    return matrix

def compute_ground_state(tree, weights, J, spins):
    """Find the ground state (as a vector of spins) and the ground state energy for an Ising spin model on a tree
    with edge weights and different interaction strengths
    """
    num_spins = max(max(tree)) + 1  # number of spins
    transfer_matrix = compute_transfer_matrix(tree, weights, J, num_spins)
    eigvals, eigvecs = eigh(transfer_matrix)
    idx = np.argmin(eigvals)
    ground_state_vec = eigvecs[:, idx]
    ground_state = np.array([1 if spin >= 0 else -1 for spin in ground_state_vec[:num_spins]])
    energy = -eigvals[idx] * len(tree)
    return ground_state, energy


def read_input(file_path):

    with open(file_path, 'r') as f:
        lines = f.readlines()

    tree = []
    weights = []
    spins = []
    J = []
    for line in lines:
        u, v, w = map(int, line.strip().split())
        weights.append(w)
        if u == v:
            spins.append(w)
        else:
            tree.append([u, v])
            J.append(w)

    return tree, weights, J, spins

def main(file_path):
    tree, weights, J, spins = read_input(file_path)
    print('tree:', tree)
    print('weights:', weights)
    print('J:', J)
    print('spins:', spins)

    ground_state, energy = compute_ground_state(tree, weights, J, spins)
    # print("Ground state:", ground_state)
    # print("Ground state energy:", energy)

if __name__ == '__main__':

    print(read_input(input_file))
    # main(file_path)
