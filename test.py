import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

order = [2, 4, 8, 16, 32, 64, 128]
alg = ['Average Naive', 'Average Strassen']
a = [2.651214599609375e-05, 0.0001149892807006836, 0.0006737947463989258, 0.002933049201965332, 0.018930935859680177, 0.14861023426055908, 1.15557918548584]
b = [1.5616416931152344e-05, 0.00030817985534667967, 0.003085756301879883, 0.016850090026855467, 0.11313693523406983, 0.8494771242141723, 6.081402683258057]

# dt = np.array([avgs_time_naive, avgs_time_strassen])
# df = np.array([order, alg, a])
# dataset = pd.DataFrame({'Order': df[0], 'Algorithm': df[1], 'Average Strassen': df[2]})
# dataset = dataset.pivot("Order", "Algorithm", "Average Strassen")

d = {
  '2': {
    'Average Naive': 2.651214599609375e-05,
    'Average Strassen': 1.5616416931152344e-05,
  },
  '4': {
    'Average Naive': 0.0001149892807006836,
    'Average Strassen': 0.00030817985534667967,
  },
  '8': {
    'Average Naive': 0.0006737947463989258,
    'Average Strassen': 0.003085756301879883,
  },
  '16': {
    'Average Naive': 0.002933049201965332,
    'Average Strassen': 0.016850090026855467,
  },
  '32': {
    'Average Naive': 0.018930935859680177,
    'Average Strassen': 0.11313693523406983,
  },
  '64': {
    'Average Naive': 0.14861023426055908,
    'Average Strassen': 0.8494771242141723,
  },
  '128': {
    'Average Naive': 1.15557918548584,
    'Average Strassen': 6.081402683258057
  }
}

ser = pd.Series(data=d, index=['2', '4', '8', '16', '32', '64', '128'])

# print(dataset)

sns.lineplot(data = ser)
plt.show()

print(ser)