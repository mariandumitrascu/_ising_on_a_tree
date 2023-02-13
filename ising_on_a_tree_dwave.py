import os
import dimod
import random
import math
from dwave.system import DWaveSampler, EmbeddingComposite
from dwave.system import LeapHybridSampler

# # Define the Ising equation
# h = {0: -1, 1: -1, 2: -1, 3: -1}
# J = {(0, 1): 1, (1, 2): 1, (1, 3): 1}

# ######################################################################################
def compute_ground_state(h, J):
    """
    Compute the ground state of the Ising equation using the D-Wave system.
    This is O(n log n) time complex algorithm and is useful for larger problems.
    """

    # Create a binary quadratic model (BQM) from the Ising equation
    bqm = dimod.BinaryQuadraticModel.from_ising(h, J)

    # Solve the BQM using the DWaveSampler
    sampler = EmbeddingComposite(DWaveSampler())
    response = sampler.sample(bqm, num_reads=1000)

    # Extract the sample with the lowest energy
    solution = next(response.samples())
    print(solution)

    # Calculate the energy of the sample with the lowest energy
    energy = bqm.energy(solution)

    return solution, energy

# ######################################################################################
def compute_ground_state_exactsolver(h, J):
    """
    Compute the ground state of the Ising equation using the ExactSolver.
    This is an O(2^n) algorithm and is only useful for small problems.
    This can be used to verify the results of the other algorithms.
    """

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
def compute_ground_state_hybridsampler(h, J):
    """
    Compute the ground state of the Ising equation using DWave quatum hybrid sampler.
    """
    # Create a binary quadratic model (BQM) from the Ising equation
    bqm = dimod.BinaryQuadraticModel.from_ising(h, J)

    # Use the LeapHybridDQMSolver to solve the BQM
    solver = LeapHybridSampler()
    sampleset = solver.sample(bqm)

    # Extract the sample with the lowest energy
    solution = sampleset.first.sample

    # Calculate the energy of the sample with the lowest energy
    energy = sampleset.first.energy

    return solution, energy

# ######################################################################################
def compute_ground_state_simulated_annealing(h, J):
    """
    Compute the ground state of the Ising equation using simulated annealing.
    This is an O(2^n) algorithm. Can be used for testing small problems.
    """

    # Define the simulated annealing parameters
    num_reads = 1000
    num_sweeps = 100
    beta_min = 0.01
    beta_max = 100
    beta_step = (beta_max - beta_min) / num_sweeps

    # Initialize the solution
    solution = {node: random.choice([-1, 1]) for node in h}

    # Define the energy function
    def calculate_energy(solution, h, J):
        energy = 0
        for node in h:
            energy += h[node] * solution[node]
        for edge in J:
            energy += J[edge] * solution[edge[0]] * solution[edge[1]]
        return energy

    # Perform simulated annealing
    for sweep in range(num_sweeps):
        beta = beta_min + sweep * beta_step
        for _ in range(num_reads):
            node = random.choice(list(h.keys()))
            old_energy = calculate_energy(solution, h, J)
            new_solution = dict(solution)
            new_solution[node] *= -1
            new_energy = calculate_energy(new_solution, h, J)
            delta_energy = new_energy - old_energy
            if delta_energy < 0 or random.random() < math.exp(-beta * delta_energy):
                solution = new_solution

    # Calculate the energy of the solution
    energy = calculate_energy(solution, h, J)

    return solution, energy

# ######################################################################################
def read_input_file(filename):
    """
    Read the input file and return the Ising equation as h and J dictionaries.
    """
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

# ######################################################################################
def dict_to_string(d):
    """
    Convert a dictionary to a string of '+' and '-' characters.
    """

    result = ''
    for i in sorted(d.keys()):
        if d[i] == 1:
            result += '+'
        else:
            result += '-'
    return result

# ######################################################################################
def main():
    """
    Main function.
    """

    script_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_path, 'sample_input.txt')

    h, J = read_input_file(file_path)

    solution, energy = compute_ground_state(h, J)

    # print(f"h = {h}")
    # print(f"J = {J}")
    # print("Solution: ", solution)
    # print("Energy: ", energy)

    solution_spins = dict_to_string(solution)

    print(energy)
    print(solution_spins)


# ######################################################################################
# ######################################################################################
# ######################################## MAIN ########################################
if __name__ == '__main__':

    main()

