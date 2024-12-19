import util
import functools


@functools.cache
def find_match(remains: str, towels: tuple) -> bool:
  if not remains:
    return True

  for t in towels:
    if remains.startswith(t):
      if find_match(remains[len(t):], towels):
        return True

  return False


def solve_1(testing: bool) -> int:
  lines = util.readfile(19, testing)
  towels = tuple([t.strip() for t in lines[0].split(',')])
  patterns = [p for p in lines[2:]]

  num_matched = 0
  for pattern in patterns:
    if find_match(pattern, towels):
      num_matched += 1

  return num_matched


def test_solve_1():
  assert solve_1(True) == 6
  assert solve_1(False) == 365


@functools.cache
def count_match(remains: str, towels: tuple) -> int:
  if not remains:
    return 1

  solutions = 0
  for t in towels:
    if remains.startswith(t):
      solutions += count_match(remains[len(t):], towels)
  return solutions


def solve_2(testing: bool) -> int:
  lines = util.readfile(19, testing)
  towels = tuple([t.strip() for t in lines[0].split(',')])
  patterns = [p for p in lines[2:]]

  solutions_count = 0
  for pattern in patterns:
    solutions_count += count_match(pattern, towels)

  return solutions_count


def test_solve_2():
  assert solve_2(True) == 16
  assert solve_2(False) == 730121486795169


if __name__ == "__main__":
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
