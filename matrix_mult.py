import numpy as np

def matrix_mult(matrix_a, matrix_b):
  matrix_c = [[sum([x*y for (x, y) in zip(line, column)]) for column in zip(*matrix_b)] for line in matrix_a]

  return np.array(matrix_c)
