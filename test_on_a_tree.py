import os
from ising_on_a_tree import compute_transfer_matrix
from ising_on_a_tree import compute_ground_state
from ising_on_a_tree import read_input


def test_transfer_matrix():
    """
    Test the transfer_matrix function
    """

    J = 1
    expected_matrix = [[1, -J, J, -1], [J, 1, -J, J], [-J, J, 1, -J], [-1, -J, J, 1]]
    actual_matrix = compute_transfer_matrix(J)
    assert expected_matrix == actual_matrix, f"Expected matrix: {expected_matrix}, but got {actual_matrix}"

# In this test, the interaction J is set to a specific value and the expected ground state is calculated manually.
# The function ground_state is then called with the specified J, and the result is compared with the expected ground state.
# If the actual ground state is not equal to the expected ground state, an error message will be printed.
def test_ground_state():
    """
    Test the ground_state function
    """

    J = 1
    expected_ground_state = [1, -1, 1, 1]
    actual_ground_state = compute_ground_state(J)
    assert expected_ground_state == actual_ground_state, f"Expected ground state: {expected_ground_state}, but got {actual_ground_state}"

# In this test, the file_path variable specifies the location of the input file,
# and the expected_input variable contains the expected input values.
# The input file is then written using the open function,
# and the read_input function is called with the specified file_path.
# The actual input is then compared with the expected input,
# and if they are not equal, an error message is printed.
# After the test is finished, the input file is automatically closed.
def test_read_input():
    # Test 1: Check the output when a valid input file is passed
    file_path = 'sample_input.txt'
    with open(file_path, 'w') as f:
        f.write('0 1 1\n')
        f.write('1 2 1\n')
        f.write('1 3 1\n')
        f.write('0 0 -1\n')
        f.write('1 1 -1\n')
        f.write('2 2 -1\n')
        f.write('3 3 -1\n')

    expected_output = ([[0, 1], [1, 2], [1, 3]], [1, 1, 1, -1, -1, -1, -1], [1, 1, 1], [-1, -1, -1, -1])
    result = read_input(file_path)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test 2: Check the output when an empty file is passed
    file_path = 'empty_input.txt'
    with open(file_path, 'w') as f:
        pass

    expected_output = ([], [], [], [])
    result = read_input(file_path)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Clean up
    os.remove(file_path)


if __name__ == '__main__':

    test_read_input()
    # test_ising_model_energy()
    # test_transfer_matrix()
    # test_ground_state()