def read_file(path):
  file = open(path, 'r')
  file = file.readlines()

  k_max = int(file[0].replace('\n', ''))
  r = int(file[1].replace('\n', ''))

  aux = file[2].replace('\n', '').split(' ')
  interval = []
  for element in aux:
    interval.append(int(element))

  return k_max, r, interval



