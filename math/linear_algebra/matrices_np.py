import numpy as np


if __name__ == "__main__":
    rotate90 = np.array([[0, -1], [1, 0]])   # CCW rotation
    v = np.array([2, 3])

    print("rotate90 @ [2,3]:", rotate90 @ v)    # [-3  2]

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[0, 1], [-1, 0]])

    print("A @ B:")
    print(A @ B)

    # Композиция: (A @ B) @ v == A @ (B @ v)
    result1 = (A @ B) @ v
    result2 = A @ (B @ v)
    print("result1:", result1)
    print("result2:", result2)
    assert np.allclose(result1, result2)
    print("Composition check passed")