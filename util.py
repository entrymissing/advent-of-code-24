def readfile(day, testing=False):
  with open(f'input/{'test' if testing else 'input'}_{day:02d}.txt') as fp:
    lines = fp.readlines()
  return [line.strip() for line in lines]