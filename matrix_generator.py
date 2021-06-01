import numpy as np

def matrix_generator(n, interval):
  matrix_a = np.random.randint(interval[0], interval[1], (n,n))
  matrix_b = np.random.randint(interval[0], interval[1], (n,n))

  return matrix_a, matrix_b