import util
import functools


def blink(number: str) -> tuple:
  if number == '0':
    return ('1',)
  if len(number) % 2 == 0:
    half_way = int(len(number)/2)
    return (number[:half_way], str(int(number[half_way:])))
  return (str(int(number) * 2024), )


def test_blink():
  assert blink('0') == ('1',)
  assert blink('1') == ('2024',)
  assert blink('131') == ('265144',)
  assert blink('10') == ('1', '0')
  assert blink('1000') == ('10', '0')


@functools.cache
def count_expansions(number: str, depth: int) -> int:
  if depth == 0:
    return 1
  count = 0
  for new_number in blink(number):
    count += count_expansions(new_number, depth-1)
  return count


def solve(testing: bool, depth: int) -> int:
  line = util.readfile(11, testing)[0]
  numbers = line.split()

  res = 0
  for number in numbers:
    res += count_expansions(number, depth)
  return res


def solve_1(testing: bool):
  return solve(testing, 25)


def test_solve_1():
  assert solve_1(True) == 55312
  assert solve_1(False) == 211306


def solve_2(testing: bool):
  return solve(testing, 75)


def test_solve_2():
  assert solve_2(False) == 250783680217283


if __name__ == '__main__':
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(False))
