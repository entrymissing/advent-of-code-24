import util


def find_trailheads(map: util.Map) -> list:
  trailheads = []
  for x in range(map.max_x):
    for y in range(map.max_y):
      if map.get(x, y) == '0':
        trailheads.append((x, y))
  return trailheads


directions = (util.Vector((1, 0)),
              util.Vector((0, 1)),
              util.Vector((-1, 0)),
              util.Vector((0, -1)))


def find_next_moves(map: util.Map,
                    pos: util.Vector,
                    height: int) -> list[util.Vector]:
  next_steps = []
  for d in directions:
    if int(map.get_vector(pos + d)) == height + 1:
      next_steps.append(pos + d)
  return next_steps


def solve(testing: bool, unique_paths: bool):
  lines = util.readfile(10, testing)
  map = util.Map(lines)
  trailheads = [util.Vector(h) for h in find_trailheads(map)]
  sum_of_summits = 0
  for head in trailheads:
    next_steps = [(head, 0)]
    summits = []
    while next_steps:
      step = next_steps.pop()
      new_steps = find_next_moves(map, step[0], step[1])
      for ns in new_steps:
        if step[1] == 8:
          summits.append(ns.get())
        else:
          next_steps.append((ns, step[1] + 1))
    if unique_paths:
      sum_of_summits += len(set(summits))
    else:
      sum_of_summits += len(summits)
  return sum_of_summits


def solve_1(testing: bool):
  return solve(testing, True)


def test_solve_1():
  assert solve_1(True) == 36
  assert solve_1(False) == 638


def solve_2(testing: bool):
  return solve(testing, False)


def test_solve_2():
  assert solve_2(True) == 81
  assert solve_2(False) == 1289


print(solve_1(True))
print(solve_1(False))
print(solve_2(True))
print(solve_2(False))
