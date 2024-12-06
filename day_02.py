import util


def is_levels_safe(levels):
  increasing = levels[0] < levels[1]
  for idx in range(len(levels)-1):
    diff = (levels[idx+1] - levels[idx])
    if diff == 0 or abs(diff) > 3:
      return False

    if increasing and diff < 0:
      return False
    if not increasing and diff > 0:
      return False
  return True


def solve_1(testing):
  lines = util.readfile(2, testing)
  all_levels = [li.split() for li in lines]

  total_safe = 0
  for levels in all_levels:
    levels = [int(v) for v in levels]
    if is_levels_safe(levels):
      total_safe += 1
  return total_safe


def test_solve_1():
  assert solve_1(True) == 2
  assert solve_1(False) == 598


def solve_2(testing):
  lines = util.readfile(2, testing)
  all_levels = [li.split() for li in lines]

  total_safe = 0
  for levels in all_levels:
    levels = [int(v) for v in levels]
    for idx in range(len(levels)):
      one_drop = levels.copy()
      del one_drop[idx]
      if is_levels_safe(one_drop):
        total_safe += 1
        break

  return total_safe


def test_solve_2():
  assert solve_2(True) == 4
  assert solve_2(False) == 634


if __name__ == '__main__':
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
