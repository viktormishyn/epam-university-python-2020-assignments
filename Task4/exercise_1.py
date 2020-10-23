# Transpose a matrix

# Test cases
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[0, 1, 9], [9, 8, 5], [7, 3, 1], [3, 4, 0]]
# matrix = [[5, 2], [8, 6], [1, 3], [9, 10], [1, 99]]


print('\nOriginal matrix:')
for i in matrix:
    print(i)


def transpose_matrix(matrix: list) -> list:
    t_matrix = []
    # The number of elements of new matrix equals the number of elements in first element of the original matrix
    length = len(matrix[0])

    index = 0
    for n in range(length):
        t_matrix.append([])
        for i in range(len(matrix)):
            t_matrix[n].append(matrix[i][index])
        index += 1
    return t_matrix


if __name__ == '__main__':
    print('\nTransposed matrix:')
    for i in transpose_matrix(matrix):
        print(i)