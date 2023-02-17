import numpy as np

def compute_ground_state(h, J):
    parent_child_states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    n = len(h)
    adj = [[] for _ in range(n)]
    for (u, v) in J:
        adj[u].append(v)
        adj[v].append(u)

    def compute_subtree(node, parent):
        energy = {1: h[node], -1: -h[node]}
        spin = {1: np.zeros(n), -1: np.zeros(n)}
        spin[1][node] = 1
        spin[-1][node] = -1

        for child in adj[node]:
            if child != parent:
                child_spin, child_energy  = compute_subtree(child, node)

                for s in parent_child_states:
                    s1, s2 = s

                    new_energy = {}
                    new_spin = {}

                    new_energy[s1] = energy[s1] + child_energy[s2] + J[(node, child)] * s1 * s2
                    new_spin[s1] = spin[s1].copy() + child_spin[s2]

                    if new_energy[s1] < energy[s1]:
                        energy[s1] = new_energy[s1]
                        spin[s1] = new_spin[s1]

        return spin, energy

    root = 0
    root_spin, root_energy  = compute_subtree(root, -1)
    min_energy = min(root_energy.values())
    min_spin_ix = min(root_energy, key=root_energy.get)
    min_spin = root_spin[min_spin_ix]
    return min_spin, min_energy

def read_input_file(filename):
    h = {}
    J = {}

    with open(filename, 'r') as f:
        for line in f:
            i, j, value = [int(x) for x in line.strip().split()]
            if i == j:
                h[i] = value
            else:
                J[(i, j)] = value
    return h, J

def array_to_string(d):
    result = ''
    for i in d:
        if i == 1:
            result += '+'
        else:
            result += '-'
    return result

def main():
    import os
    script_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_path, 'sample_input.txt')
    h, J = read_input_file(file_path)
    solution, energy  = compute_ground_state(h, J)
    solution_spins = array_to_string(solution)
    print(energy)
    print(solution_spins)

if __name__ == '__main__':
    main()
