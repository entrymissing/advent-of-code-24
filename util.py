def readfile(day, testing=False, suffix=None):
  filename = f'input/{'test' if testing else 'input'}_{day:02d}.txt'
  if suffix:
    filename = filename[:-4] + f'-{suffix}.txt'
  with open(filename) as fp:
    lines = fp.readlines()
  return [line.strip() for line in lines]


class Map(object):
  def __init__(self, map_lines):
    # Transpose the map (to make the first list index dimension X)
    map_lines = list(map(list, zip(*map_lines)))
    self.map = [list(row) for row in map_lines]
    self.max_x = len(self.map)
    self.max_y = len(self.map[0])

  def __str__(self):
    res = ''
    for row in self.map:
      res += ''.join(row) + '\n'
    return res

  def get(self, x, y, out_of_bounds_return_value=False):
    if x < 0 or y < 0:
      return out_of_bounds_return_value
    if x >= self.max_x or y >= self.max_y:
      return out_of_bounds_return_value
    return self.map[x][y]

  def set(self, x, y, value):
    self.map[x][y] = value
