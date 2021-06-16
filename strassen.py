import numpy as np
from numpy.lib.nanfunctions import nanargmax
from matrix_mult import matrix_mult

def strassen(hybrid, matrix_a, matrix_b):
  shape = matrix_a.shape
  n = shape[0]
  
  if hybrid and n <= 5:
    return matrix_mult(matrix_a, matrix_b)
  elif n <= 2:
    return matrix_mult_base(matrix_a, matrix_b)
  else:
    A11, A12, A21, A22 = split_matrix(n, matrix_a)
    B11, B12, B21, B22 = split_matrix(n, matrix_b)
    
    M1 = strassen(hybrid, addMatrices(A11,A22), addMatrices(B11,B22))
    M2 = strassen(hybrid, addMatrices(A21, A22), B11)
    M3 = strassen(hybrid, A11, addMatrices(B12, -B22))
    M4 = strassen(hybrid, A22, addMatrices(B21, -B11))
    M5 = strassen(hybrid, addMatrices(A11, A12), B22)
    M6 = strassen(hybrid, addMatrices(A21, -A11), addMatrices(B11, B12))
    M7 = strassen(hybrid, addMatrices(A12, -A22), addMatrices(B21, B22))
    
    C11 = addMatrices(addMatrices(M1, M4), addMatrices(-M5, M7))
    C12 = addMatrices(M3, M5)
    C21 = addMatrices(M2, M4)
    C22 = addMatrices(addMatrices(M1, -M2), addMatrices(M3, M6))

  matrix_c = np.concatenate((np.concatenate((C11, C12), axis=1), np.concatenate((C21, C22), axis=1)), axis = 0 )
  return np.array(matrix_c)

def split_matrix(n, matrix):
  half = int(n/2)
  
  A11 = [[matrix[l,c] for c in range(n) if c <  half] for l in range(n) if l <  half]
  A12 = [[matrix[l,c] for c in range(n) if c >= half] for l in range(n) if l <  half]
  A21 = [[matrix[l,c] for c in range(n) if c <  half] for l in range(n) if l >= half]
  A22 = [[matrix[l,c] for c in range(n) if c >= half] for l in range(n) if l >= half]

  return np.array(A11), np.array(A12), np.array(A21), np.array(A22)

def addMatrices(matrix_a, matrix_b):
  shape = matrix_a.shape
  n = shape[0]

  matrix_c = [[matrix_a[l, c] + matrix_b[l, c] for c in range(n)] for l in range(n)]

  return np.array(matrix_c)
  
def matrix_mult_base(matrix_a, matrix_b):
  C11 = (matrix_a[0,0] * matrix_b[0,0]) + (matrix_a[0,1] * matrix_b[1,0]) 
  C12 = (matrix_a[0,0] * matrix_b[0,1]) + (matrix_a[0,1] * matrix_b[1,1])
  C21 = (matrix_a[1,0] * matrix_b[0,0]) + (matrix_a[1,1] * matrix_b[1,0])
  C22 = (matrix_a[1,0] * matrix_b[0,1]) + (matrix_a[1,1] * matrix_b[1,1])

  matrix_c = [[C11, C12], [C21, C22]]
  return np.array(matrix_c)
