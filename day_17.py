import util


def get_combo_operand(operand: int, a: int, b: int, c: int) -> int:
  combo = 0
  match operand:
    case 0 | 1 | 2 | 3:
      combo = operand
    case 4:
      combo = a
    case 5:
      combo = b
    case 6:
      combo = c
    case _:
      raise ValueError(f'operand was {operand}')
  return combo


def execute(inst: int, operand: int, a: int, b: int, c: int) -> tuple:
  jump = None
  out = None
  match inst:
    case 0:
      a = int(a / 2 ** get_combo_operand(operand, a, b, c))
    case 1:
      b = b ^ operand
    case 2:
      b = get_combo_operand(operand, a, b, c) % 8
    case 3:
      if a != 0:
        jump = operand
    case 4:
      b = b ^ c
    case 5:
      out = get_combo_operand(operand, a, b, c) % 8
    case 6:
      b = int(a / 2 ** get_combo_operand(operand, a, b, c))
    case 7:
      c = int(a / 2 ** get_combo_operand(operand, a, b, c))
    case _:
      raise ValueError(f'instruction was {inst}')
  return (a, b, c, jump, out)


def test_execute():
  assert execute(2, 6, None, None, 9) == (None, 1, 9, None, None)
  assert execute(5, 0, None, None, None) == (None, None, None, None, 0)


def run_program(codes: list, a: int, b: int, c: int) -> list:
  outputs = []

  ptr = 0
  while ptr < len(codes):
    # print(ptr, codes[ptr], codes[ptr+1], a, b, c)
    a, b, c, jump, out = execute(codes[ptr], codes[ptr+1], a, b, c)
    if jump is not None:
      ptr = jump
    else:
      ptr += 2
    if out is not None:
      outputs.append(out)
  return outputs


def test_run_program():
  assert run_program([5, 0, 5, 1, 5, 4], 10, None, None) == [0, 1, 2]
  assert run_program([0, 1, 5, 4, 3, 0], 2024, None, None) == [4, 2, 5, 6, 7,
                                                               7, 7, 7, 3, 1,
                                                               0]


def solve_1(testing: bool) -> int:
  lines = util.readfile(17, testing)
  a = int(lines[0].split()[-1])
  b = int(lines[1].split()[-1])
  c = int(lines[2].split()[-1])
  codes = [int(v) for v in lines[4].split()[-1].split(',')]
  return ','.join([str(v) for v in run_program(codes, a, b, c)])


def test_solve_1():
  assert solve_1(True) == '4,6,3,5,6,3,5,2,1,0'
  assert solve_1(False) == '3,4,3,1,7,6,5,6,0'


def solve_2(testing: bool) -> int:
  lines = util.readfile(17, testing)
  codes = [int(v) for v in lines[4].split()[-1].split(',')]

  found_digits = 2
  found_x = 24
  while found_digits < len(codes):
    found_digits += 1
    for curX in range(found_x*8, found_x*8*8):
      prog = run_program(codes, curX, 0, 0)
      if prog[(-1*found_digits):] == codes[(-1*found_digits):]:
        found_x = curX
        break
  return found_x


def test_solve_2():
  assert solve_2(False) == 109019930331546


if __name__ == "__main__":
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(False))
