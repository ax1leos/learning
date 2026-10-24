# NumPy notes

## Array basics

- `np.array([1, 2, 3])` creates a 1D array.
- `.shape` — размеры массива.
- `.dtype` — тип элементов.
- `np.zeros((2, 3))` — матрица 2x3 из нулей.
- `np.arange(0, 10, 2)` — [0 2 4 6 8].

## Operations

- Element-wise addition: `a + b`
- Scalar multiplication: `k * a`
- Matrix @ vector: `M @ v`  (@ = matmul)
- Matrix @ matrix: `A @ B`
- Compare arrays: `np.allclose(a, b)`
- Transpose: `a.T`

## Storage

- NumPy stores matrices as 2D arrays in ROW order (as in textbooks).
- For NumPy, write `[[0, -1], [1, 0]]` — this is the standard.
- Old `matrices.py` (Day 13) used COLUMNS — different convention.
- If needed, transpose with `.T`.

## Useful to remember

- `@` = matrix multiplication.
- `*` = element-wise multiplication.
- `np.allclose(a, b)` — for comparing arrays (not `==`).