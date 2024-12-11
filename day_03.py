import util
import re


def parse_program(input):
  res = 0
  mults = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
  for mult in mults:
    a, b = mult[4:-1].split(',')
    res += int(a) * int(b)
  return res


def solve_1(testing):
  lines = util.readfile(3, testing)
  line = ''.join(lines)

  res = 0
  for line in lines:
    res += parse_program(line)
  return res


def test_solve_1():
  assert solve_1(True) == 161
  assert solve_1(False) == 187833789


def solve_2(testing, suffix=None):
  lines = util.readfile(3, testing, suffix)
  line = ''.join(lines)
  line = f'do(){line}don\'t()'

  res = 0
  parts = re.findall(r'do\(\).*?don\'t\(\)', line)
  for part in parts:
    res += parse_program(part)
  return res


def test_solve_2():
  assert solve_2(True) == 161
  assert solve_2(True, 2) == 48
  assert solve_2(False) == 94455185


if __name__ == '__main__':
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True, 2))
  print(solve_2(False))
