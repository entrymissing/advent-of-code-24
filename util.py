def readfile(day, testing=False, suffix=None):
  filename = f'input/{'test' if testing else 'input'}_{day:02d}.txt'
  if suffix:
    filename = filename[:-4] + f'-{suffix}.txt'
  with open(filename) as fp:
    lines = fp.readlines()
  return [line.strip() for line in lines]