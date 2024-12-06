import util


def parse_lines(lines):
  left = []
  right = []
  for line in lines:
    l, r = line.strip().split()
    left.append(int(l))
    right.append(int(r))
  return left, right


def test_parse_lines():
  assert parse_lines(['1 2', '3 4']) == ([1, 3], [2, 4])


def solve_1(testing):
  lines = util.readfile(1, testing)

  left, right = parse_lines(lines)

  diff = 0
  for le, r in zip(sorted(left), sorted(right)):
    diff += abs(le-r)
  return diff


def test_solve_1():
  assert solve_1(True) == 11
  assert solve_1(False) == 2164381


def solve_2(testing):
  lines = util.readfile(1, testing)

  left, right = parse_lines(lines)

  res = 0
  for le in left:
      c = right.count(le)
      res += c * le
  return res


def test_solve_2():
  assert solve_2(True) == 31
  assert solve_2(False) == 20719933


print(solve_1(True))
print(solve_1(False))
print(solve_2(True))
print(solve_2(False))
