def add(v, w):
    return [v[0]+w[0], v[1]+w[1]]

def scale(k, v):
    return [k * v[0], k * v[1]]

def linear_combination(a, v, b, w):
    return add(scale(a,v), scale(b, w))

v = [2, 3]
w = [-1, 1]

print(add(v, w))
print(scale(3, v))
print(linear_combination(2, v, -1, w))