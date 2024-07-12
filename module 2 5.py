def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for i in range(m):
            matrix.append(value)
    return matrix


matrix = get_matrix(3,5, 42)
print(matrix)




