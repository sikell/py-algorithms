def matrix_print(matrix):
    return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix])
