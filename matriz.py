import numpy as np

def print_matrix(title_matrix, matrix):
    string_matrix = np.array2string(matrix, separator=', ')
    print(title_matrix + ":\n " + string_matrix)

def generate_actual_frame(previous_frame):
    row, column = previous_frame.shape
    actual_frame = previous_frame.copy()
    num_changes = np.size(actual_frame) // 3
    indices_to_change = [(np.random.randint(0, row), np.random.randint(0, column)) for _ in range(num_changes)]
    
    for i, j in indices_to_change:
        actual_frame[i][j] = np.random.randint(0, 101)
    
    return actual_frame

def compare_matrix(matrix1, matrix2):
    return np.abs(matrix1 - matrix2)

def find_max_value_submatrix(binary_matrix):
    sub_matrix_size = 4
    
    max_sum = 0
    max_submatrix_coords = (0, 0)

    for i in range(binary_matrix.shape[0] - sub_matrix_size + 1):
        for j in range(binary_matrix.shape[1] - sub_matrix_size + 1):
            window = binary_matrix[i:i+sub_matrix_size, j:j+sub_matrix_size]
            window_sum = np.sum(window)
            
            if window_sum > max_sum:
                max_sum = window_sum
                max_submatrix_coords = (i, j)

    return max_submatrix_coords

def mark_max_difference_region(binary_matrix, max_submatrix_coords, sub_matrix_size):
    i, j = max_submatrix_coords
    binary_matrix[i:i+sub_matrix_size, j:j+sub_matrix_size] = 1
    return binary_matrix

i = 0
while i < 10:
    print("--------------------------------")
    print("Test nº" + str(i + 1))
    row_value = np.random.randint(2, 10) 
    column_value = np.random.randint(2, 10)  
    previous_frame = np.random.randint(1, 10, size=(row_value, column_value))
    actual_frame = generate_actual_frame(previous_frame)

    print_matrix("Previous Frame", previous_frame)
    print_matrix("Actual Frame", actual_frame)
    
    difference_matrix = compare_matrix(actual_frame, previous_frame)
    print_matrix("Difference Matrix", difference_matrix)
    
    max_submatrix_coords = find_max_value_submatrix(difference_matrix)
    print("Coordinates of max difference sub-matrix:", max_submatrix_coords)
    
    result_matrix = np.zeros_like(difference_matrix)
    result_matrix = mark_max_difference_region(result_matrix, max_submatrix_coords, sub_matrix_size=4)
    print_matrix("Result Matrix", result_matrix)

    i += 1
