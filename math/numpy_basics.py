import numpy as np

# Создание массивов
a = np.array([1, 2, 3, 4])
print(a)
print(a.shape)   # (4,)
print(a.dtype)   # int64

b = np.zeros((2, 3))
print(b)         # [[0. 0. 0.] [0. 0. 0.]]

c = np.arange(0, 10, 2)
print(c)         # [0 2 4 6 8]

# Срезы
d = np.array([[1, 2, 3], [4, 5, 6]])
print(d[0, :])   # [1 2 3]
print(d[:, 1])   # [2 5]

e = np.linspace(0, 10, num=5, dtype = np.int64)
print(e)    # [ 0  2  5  7 10]

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))     # [1, 2, 3, 4, 5, 6, 7, 8]

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((a, b)))   # [1, 2, 3, 4, 5, 6, 7, 8]
print(np.concatenate((x, y), axis=0))   # [[1, 2],
                                        # [3, 4], 
                                        # [5, 6]]
                                        
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(array_example.ndim)   # 3
print(array_example.size)   # 24
print(array_example.shape)  # (3, 2, 4)

a = np.arange(6)
print(a)    # [0 1 2 3 4 5]

a = np.arange(6)
b = a.reshape(3, 2)
print(b)    # [[0 1]
            # [2 3]
            # [4 5]]
            
a = np.arange(6)
print(np.reshape(a, shape=(1, 6), order='C'))   # [[0, 1, 2, 3, 4, 5]]

a = np.array([1, 2, 3, 4, 5, 6])
a2 = a[np.newaxis, :]
print(a2.shape) # (1, 6)
col_vector = a[:, np.newaxis]
print(col_vector.shape) # (6, 1)

a = np.array([1, 2, 3, 4, 5, 6])
b = np.expand_dims(a, axis=1)
print(b.shape)  # (6, 1)
c = np.expand_dims(a, axis=0)
print(c.shape) # (1, 6)

data = np.array([1, 2, 3])
print(data[1])  # 2
print(data[0:2])    # [1, 2]
print(data[1:]) # [2, 3]
print(data[-2:])    # [2, 3]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5]) # [1 2 3 4]
print(a[a >= 5])    # [ 5  6  7  8  9 10 11 12]
print(a[a%2==0])    # [ 2  4  6  8 10 12]
print(a[(a > 2) & (a < 11)])    # [ 3  4  5  6  7  8  9 10]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print((a > 5) | (a == 5))   # [[False False False False]
                            # [ True  True  True  True]
                            # [ True  True  True True]]
                            
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)    # (array([0, 0, 0, 0]), array([0, 1, 2, 3]))
print(list(zip(*b)))    # [(np.int64(0), np.int64(0)),
                        # (np.int64(0), np.int64(1)),
                        # (np.int64(0), np.int64(2)),
                        # (np.int64(0), np.int64(3))]
print(a[b]) # [1 2 3 4] - для вывода элементов массива, количество которых меньше 5

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
not_there = np.nonzero(a == 42)
print(not_there)    # (array([], dtype=int64), array([], dtype=int64))