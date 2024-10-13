# Матрица воплоти

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(value)
        matrix.append(line)
    return matrix

rez1 = get_matrix(2, 2, 10)

print('Матрицв1: ', rez1)    
print('Матрицв2: ', get_matrix(3, 5, 42))           
print('Матрицв3: ', get_matrix(4, 2, 13))   
