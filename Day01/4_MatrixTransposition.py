originalMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposedMatrix = []
    for _ in range(cols):
        transposedMatrix.append([])

    for i in range(rows):
        for j in range(cols):
            transposedMatrix[j].append(matrix[i][j])

    return transposedMatrix

transposedMatrix = transpose(originalMatrix)

print("Original Matrix:")
for row in originalMatrix:
    print(row)

print()

print("Transposed Matrix:")
for row in transposedMatrix:
    print(row)