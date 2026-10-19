# Linear Algebra — Notes

## Video 1 — Vectors, what even are they?

- A vector is an arrow from the origin: it has a **direction** and a **length**.
- Vector [2, 3] means "2 steps right, 3 steps up" (in 2D).
- In linear algebra, the vector is thought of as the arrow itself, not just as a pair of numbers.
- The origin is the point (0, 0). Every vector starts there.

## Video 2 — Linear combinations, span, and basis vectors

### Linear combination

A **linear combination** of vectors v and w is:

    a·v + b·w

where a and b are numbers (called **coefficients**).

Meaning: scale v by a, scale w by b, then add the results.

Example:
    2·[2, 3] + (-1)·[-1, 1]
    = [4, 6] + [1, -1]
    = [5, 5]

### Span

The **span** of v and w is the set of **all possible linear combinations** a·v + b·w.

- If v and w are not parallel → span is the whole plane.
- If v and w are parallel → span is just a line.

### Basis

A **basis** is a set of vectors that can produce **any** other vector as a linear combination.

The standard basis in 2D:
    [1, 0] and [0, 1]

Any vector can be written as a combination of these:
    [3, 5] = 3·[1, 0] + 5·[0, 1]

### Code

See `vectors.py`:
- `add(v, w)` — add two vectors.
- `scale(k, v)` — multiply vector by a number.
- `linear_combination(a, v, b, w)` — return a·v + b·w.

## Video 3 — Linear transformations and matrices

**Main idea:** A matrix is a rule for transforming space. The columns
tell you where the basis vectors [1,0] and [0,1] land after the transformation.

**Two questions answered:**

1. What does the first column of a matrix show?
   Coordinates of "i" basis after transformation.

2. Why does matrix-vector multiplication give a*x + b*y?
   Because it's a linear combination of the matrix columns:
   x times first column + y times second column.
   The columns are where basis vectors i and j land after transformation.
   So the result is x steps along new i plus y steps along new j.