import util
import re
import statistics


def get_quadrant(pos: util.Vector, mid_x: int, mid_y: int):
  x, y = pos.get()

  if x == mid_x or y == mid_y:
    return -1
  return int(x > mid_x) + 2 * int(y > mid_y)


def solve_1(testing: bool, plot_size: util.Vector) -> int:
  lines = util.readfile(14, testing)
  sx, sy = plot_size.get()
  mx, my = int(sx / 2), int(sy / 2)
  steps = 100

  quadrants = [0, 0, 0, 0]

  for line in lines:
    numbers = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', line)
    p = util.Vector((int(numbers[0]), int(numbers[1])))
    d = util.Vector((int(numbers[2]), int(numbers[3])))
    dest = (p + d * steps) % plot_size
    q = get_quadrant(dest, mx, my)
    if q >= 0:
      quadrants[q] += 1

  safety_factor = 1
  for q in quadrants:
    safety_factor *= q
  return safety_factor


def test_solve_1():
  assert solve_1(True, util.Vector((11, 7))) == 12
  assert solve_1(False, util.Vector((101, 103))) == 216027840


def render_bots(positions: set, plot_size: util.Vector):
  for x in range(plot_size.get_dim(0)):
    for y in range(plot_size.get_dim(1)):
      if (x, y) in positions:
        print('X', end='')
      else:
        print('.', end='')
    print('')


def get_center_mass(positions: set):
  x = []
  y = []
  for cx, cy in positions:
    x.append(cx)
    y.append(cy)
  return statistics.variance(x) + statistics.variance(y)


def solve_2(testing: bool, plot_size: util.Vector) -> int:
  lines = util.readfile(14, testing)

  starts = []
  dirs = []

  for line in lines:
    numbers = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', line)
    starts.append(util.Vector((int(numbers[0]), int(numbers[1]))))
    dirs.append(util.Vector((int(numbers[2]), int(numbers[3]))))

  step = 1

  while True:
    positions = set()
    for s, d in zip(starts, dirs):
      positions.add((((s+d*step) % plot_size)).get())

    dive = get_center_mass(positions)
    if dive < 1000:
      return step
    step += 1


if __name__ == "__main__":
  print(solve_1(True, util.Vector((11, 7))))
  print(solve_1(False, util.Vector((101, 103))))
  print(solve_2(False, util.Vector((101, 103))))
