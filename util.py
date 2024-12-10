def readfile(day, testing=False, suffix=None):
  filename = f'input/{"test" if testing else "input"}_{day:02d}.txt'
  if suffix:
    filename = filename[:-4] + f'-{suffix}.txt'
  with open(filename) as fp:
    lines = fp.readlines()
  return [line.strip() for line in lines]


class Vector(object):
  def __init__(self, pos):
    self.pos = tuple(pos)

  def __add__(self, other):
    return Vector([a+b for a, b in zip(self.pos, other.get())])

  def __sub__(self, other):
    return Vector([a-b for a, b in zip(self.pos, other.get())])

  def __mul__(self, other):
    if isinstance(other, int):
      return Vector([a*other for a in self.pos])
    raise ValueError()

  def __str__(self):
    return f'{self.pos}'

  def get(self):
    return self.pos

  def get_dim(self, dim: int) -> int:
    return self.pos[dim]


def test_vector():
  a = Vector([1, 2])
  b = Vector([3, 4])

  assert a.get() == (1, 2)
  assert b.get() == (3, 4)

  assert (a+b).get() == (4, 6)
  assert (a+b).get() == (b+a).get()

  assert (a-b).get() == (-2, -2)
  assert (b-a).get() == (2, 2)

  assert (a*3).get() == (3, 6)


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

  def get(self, x: int, y: int, out_of_bounds_return_value=False):
    if x < 0 or y < 0:
      return out_of_bounds_return_value
    if x >= self.max_x or y >= self.max_y:
      return out_of_bounds_return_value
    return self.map[x][y]

  def get_vector(self, pos: Vector, out_of_bounds_return_value=False):
    return self.get(pos.get_dim(0), pos.get_dim(1), out_of_bounds_return_value)

  def set(self, x, y, value):
    self.map[x][y] = value
