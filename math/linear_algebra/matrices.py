def apply(matrix, vector):
    x, y = vector
    (a, c), (b, d) = matrix # (a, c) - column, (a, b) - row
    return [x * a + y * b, x * c + y * d]

rotate90 = [[0, 1], [-1, 0]] # [0, 1] and [-1, 0] - columns
scale2 = [[2, 0], [0, 2]]
shear = [[1, 1], [0, 1]]

print(apply(rotate90, [2,3]))
print(apply(scale2, [2,3]))
print(apply(shear, [2,3]))