import util
import copy

def get_start(map):
  for x in range(map.max_x):
    for y in range(map.max_y):
      if map.get(x, y) == '^':
        return (x,y)

directions = ((0,-1), (1,0), (0,1), (-1,0))

def get_path(map):
  x,y = get_start(map)
  is_loop = False
  dir_idx = 0
  path = [(x, y, directions[dir_idx][0],  directions[dir_idx][1])]
  next_x = x + directions[dir_idx][0]
  next_y = y + directions[dir_idx][1]

  while map.get(next_x, next_y):
    if map.get(next_x, next_y) == '#':
      dir_idx = (dir_idx + 1) % 4
      next_x = x + directions[dir_idx][0]
      next_y = y + directions[dir_idx][1]
      continue
    x = next_x
    y = next_y
    next_x = x + directions[dir_idx][0]
    next_y = y + directions[dir_idx][1]
    cur_step = (x, y, directions[dir_idx][0],  directions[dir_idx][1])
    if cur_step in path:
      is_loop = True
      break
    path.append(cur_step)

  return set([(p[0], p[1]) for p in path]), is_loop

def solve_1(testing):
  lines = util.readfile(6, testing)
  map = util.Map(lines)

  return len(get_path(map)[0])

def test_solve_1():
  assert solve_1(True) == 41
  assert solve_1(False) == 5067

def solve_2(testing):
  lines = util.readfile(6, testing)
  map = util.Map(lines)
  
  x,y = get_start(map)
  path = get_path(map)[0]

  count_loops = 0
  for idx, step in enumerate(path):
    if step == (x, y):
      continue
    new_map = copy.deepcopy(map)
    new_map.set(step[0], step[1], '#')
    if get_path(new_map)[1]:
      count_loops += 1
  return count_loops

def test_solve_2():
  assert solve_2(True) == 6


print(solve_1(True))
print(solve_1(False))
print(solve_2(True))
# All hail brute force .. correct but slow
# print(solve_2(False))
