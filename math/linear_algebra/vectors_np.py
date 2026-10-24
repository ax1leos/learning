import numpy as np


def add(v, w):
    return v + w


def scale(k, v):
    return k * v


def linear_combination(a, v, b, w):
    return a * v + b * w


if __name__ == "__main__":
    v = np.array([2, 3])
    w = np.array([-1, 1])

    print("add:", add(v, w))    # [1 4]
    print("scale:", scale(2, v))    # [4 6]
    print("linear_combination:", linear_combination(2, v, -1, w))   # [5 5]

    assert np.allclose(add(v, w), [1, 4])
    assert np.allclose(scale(2, v), [4, 6])
    assert np.allclose(linear_combination(2, v, -1, w), [5, 5])
    print("All checks passed")