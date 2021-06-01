import sys
import time
import seaborn as sns
import matplotlib.pyplot as plt

from read_file import read_file
from matrix_generator import matrix_generator
from matrix_mult import matrix_mult
from strassen import *

path = sys.argv[1]

k_max, r, interval = read_file(path)

avgs_time_naive = []
avgs_time_strassen = []
avgs_time_hybrid_strassen = []

# Função para plotar o gráfico
def plot_graph(k_max, avg_naive, avg_strassen, avg_hybrid_strassen):
  x = list(range(1, k_max + 1))
  a = sns.lineplot(x, avg_naive, label="Naive")
  a = sns.lineplot(x, avg_strassen, label="Strassen")
  a = sns.lineplot(x, avg_hybrid_strassen, label="Strassen Hybrid")
  a.set(xlabel='Tamanho da entrada 2^', ylabel='tempo de execução médio (s)')
  a.legend()
  plt.show()

# O k_max das matrízes é dada por k = 5
for order in range(1, k_max + 1):
    # n -> dimensões da matrix nxn
    n = 2 ** order
    times_naive = 0
    times_strassen = 0
    times_hybrid_strassen = 0

    avg_time_naive = 0
    avg_time_strassen = 0
    avg_time_hybrid_strassen = 0

    # r -> quantidade de matrizes que serão geradas
    # e multiplicadas
    for i in range(0, r):
      matrix_a, matrix_b = matrix_generator(n, interval)

      initial_time_strassen = time.time()
      strassen(0, matrix_a, matrix_b)
      final_time_strassen = time.time()
      times_strassen += final_time_strassen - initial_time_strassen

      initial_time_hybrid_strassen = time.time()
      strassen(1, matrix_a, matrix_b)
      final_time_hybrid_strassen = time.time()
      times_hybrid_strassen += final_time_hybrid_strassen - initial_time_hybrid_strassen

      initial_time = time.time()
      matrix_mult(matrix_a, matrix_b)
      final_time = time.time()
      times_naive += final_time - initial_time

    # calculando a média de tempo de execução das
    # multiplicações de matrizes para a ordem atual
    avg_time_naive = times_naive/r
    avg_time_strassen = times_strassen/r
    avg_time_hybrid_strassen = times_hybrid_strassen/r

    avgs_time_naive.append(avg_time_naive)
    avgs_time_strassen.append(avg_time_strassen)
    avgs_time_hybrid_strassen.append(avg_time_hybrid_strassen)
    print('media order 2^{} -> strassen: {} \thybrid: {} \tnaive: {}'.format(order, avg_time_strassen, avg_time_hybrid_strassen, avg_time_naive))

plot_graph(k_max,
  [x/r for x in avgs_time_naive],
  [x/r for x in avgs_time_strassen],
  [x/r for x in avgs_time_hybrid_strassen])
