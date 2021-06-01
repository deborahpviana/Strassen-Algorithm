import numpy as np
from numpy.core.fromnumeric import shape

def matrix_mult(matrix_a, matrix_b):
  shape = matrix_a.shape
  n = shape[0]

  matrix_c = []

  for content in matrix_a:
    c_line = []
    for colum in range(0, n):
      res = 0
      for line, element in enumerate(content):
        res += element * matrix_b[line, colum]

      c_line.append(res)
    
    matrix_c.append(c_line.copy())

  return np.array(matrix_c)

