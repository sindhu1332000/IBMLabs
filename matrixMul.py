matrix1 = [[3, 6, 9],
           [12, 5, 7],
           [7, 8, 4]]
matrix2 = [[12, 6, 7, 9],
           [4, 0, 8, 7],
           [5, 4, 1, 9]]
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k]*matrix2[k][j]
for r in result:
    print(r)