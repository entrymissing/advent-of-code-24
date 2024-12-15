import util


def parse_input(lines: list, double_size=False) -> tuple:
  map_lines = []
  while True:
    curLine = lines.pop(0).strip()
    if not curLine:
      break
    if double_size:
      curLine = curLine.replace('#', '##')
      curLine = curLine.replace('O', '[]')
      curLine = curLine.replace('.', '..')
      curLine = curLine.replace('@', '@.')
    map_lines.append(curLine)
  map = util.Map(map_lines)

  directions = ''
  while lines:
    curLine = lines.pop(0).strip()
    directions += curLine
  return map, directions


dir_map = {'>': util.Vector((1, 0)),
           '^': util.Vector((0, -1)),
           '<': util.Vector((-1, 0)),
           'v': util.Vector((0, 1))
           }


def move_block(map: util.Map, pos: util.Vector, d: util.Vector):
  from_val = map.get_vector(pos)
  to_val = map.get_vector(pos + d)
  if to_val == '.':
    map.set_vector(pos + d, from_val)
    if from_val == '@':
      map.set_vector(pos, '.')
    return True

  if to_val == '#':
    return False

  if to_val == 'O':
    if move_block(map, pos + d, d):
      map.set_vector(pos + d, from_val)
      if from_val == '@':
        map.set_vector(pos, '.')
      return True
    return False


def sum_coords(map: util.Map):
  res = 0
  for x in range(map.max_x):
    for y in range(map.max_y):
      if map.get(x, y) in ['O', '[']:
        res += 100 * y + x
  return res


def solve_1(testing: bool) -> int:
  lines = util.readfile(15, testing)
  map, directions = parse_input(lines)

  pos = util.Vector(map.find_first('@'))
  for d in directions:
    moved = move_block(map, pos, dir_map[d])
    if moved:
      pos = pos + dir_map[d]
  return sum_coords(map)


def test_solve_1():
  assert solve_1(True) == 10092
  assert solve_1(False) == 1495147


def can_move(map: util.Map, pos: util.Vector, d: util.Vector) -> bool:
  if map.get_vector(pos + d) == '.':
    return True

  if map.get_vector(pos + d) == '#':
    return False

  if d == util.LEFT or d == util.RIGHT:
    if map.get_vector(pos + d) in ['[', ']']:
      return can_move(map, pos + d*2, d)

  if d == util.UP or d == util.DOWN:
    if map.get_vector(pos + d) == '[':
      return can_move(map, pos + d, d) \
        and can_move(map, pos + d + util.RIGHT, d)

    if map.get_vector(pos + d) == ']':
      return can_move(map, pos + d, d) \
        and can_move(map, pos + d + util.LEFT, d)


def move_big_blocks(map: util.Map, pos: util.Vector, d: util.Vector):
  if d == util.LEFT or d == util.RIGHT:
    if map.get_vector(pos + d) in ['[', ']']:
      move_big_blocks(map, pos + d * 2, d)
      move_big_blocks(map, pos + d, d)

  if d == util.UP or d == util.DOWN:
    if map.get_vector(pos + d) == '[':
      move_big_blocks(map, pos + d, d)
      move_big_blocks(map, pos + d + util.RIGHT, d)

    if map.get_vector(pos + d) == ']':
      move_big_blocks(map, pos + d, d)
      move_big_blocks(map, pos + d + util.LEFT, d)

  val_to = map.get_vector(pos + d)
  val_from = map.get_vector(pos)
  map.set_vector(pos, val_to)
  map.set_vector(pos+d, val_from)


def solve_2(testing: bool) -> int:
  lines = util.readfile(15, testing)
  map, directions = parse_input(lines, True)

  pos = util.Vector(map.find_first('@'))
  for d in directions:
    if can_move(map, pos, dir_map[d]):
      move_big_blocks(map, pos, dir_map[d])
      pos = pos + dir_map[d]

  return sum_coords(map)


def test_solve_2():
  assert solve_2(True) == 9021
  assert solve_2(False) == 1524905


if __name__ == "__main__":
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
