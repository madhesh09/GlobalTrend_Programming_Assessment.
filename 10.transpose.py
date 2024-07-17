def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) 
    
    trans = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        trans.append(new_row)
    
    return trans
matrix = [
    [1, 2],
    [4, 5]
]

transposed_matrix = transpose(matrix)

print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)

