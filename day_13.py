import util


def solve(testing: bool, offset=0) -> int:
  lines = util.readfile(13, testing)

  tokens = 0
  while lines:
    a_line = lines.pop(0).split('+')[1:]
    a = int(a_line[0].split(',')[0])
    b = int(a_line[1])

    b_line = lines.pop(0).split('+')[1:]
    c = int(b_line[0].split(',')[0])
    d = int(b_line[1])

    price_line = lines.pop(0).split('=')[1:]
    e = int(price_line[0].split(',')[0])
    f = int(price_line[1])

    if offset:
      e, f = e+offset, f+offset

    y = (f - ((b*e)/a)) / (d - ((b*c)/a))
    x = (e-y*c) / a

    if lines:
      lines.pop(0)

    # checking for colinearity, which never happens
    if a*d + b*c == 0:
      continue

    if abs(y - round(y)) < 0.001 and abs(x - round(x)) < 0.001:
      x, y = round(x), round(y)
      if x < 0 or y < 0:
        print(x, y)
      if offset or (x <= 100 and y <= 100):
        tokens += 3 * x + y

  return tokens


def solve_1(testing: bool) -> int:
  return solve(testing)


def test_solve_1():
  assert solve_1(True) == 480
  assert solve_1(False) == 27105


def solve_2(testing: bool) -> int:
  return solve(testing, 10000000000000)


def test_solve_2():
  assert solve_2(False) == 101726882250942


if __name__ == "__main__":
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(False))
