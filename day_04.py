import util
from collections import defaultdict

all_directions = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))
x_directions = ((1,1), (1,-1), (-1,-1), (-1,1))

def search_mas_in_direction(map, x, y, direction, offset=1):
  for step, c in enumerate('MAS'):
    new_x = x + (step+offset) * direction[0]
    new_y = y + (step+offset) * direction[1]
    if map.get(new_x, new_y) != c:
      return False
  return True

def solve_1(testing):
  lines = util.readfile(4, testing)
  map = util.Map(lines)

  xmas_count = 0
  for x in range(map.max_x):
    for y in range(map.max_y):
      if map.get(x,y) == 'X':
        for d in all_directions:
          if search_mas_in_direction(map, x, y, d):
            xmas_count += 1
  return xmas_count

def test_solve_1():
  assert solve_1(True) == 18
  assert solve_1(False) == 2547

def solve_2(testing):
  lines = util.readfile(4, testing)
  map = util.Map(lines)

  mas_location = defaultdict(int)
  for x in range(map.max_x):
    for y in range(map.max_y):
      for d in x_directions:
        if search_mas_in_direction(map, x, y, d, 0):
          mas_location[(x+d[0], y+d[1])] += 1
  
  xmas_count = 0
  for loc in mas_location:
    if mas_location[loc] == 2:
      xmas_count += 1
  return xmas_count

def test_solve_2():
  assert solve_2(True) == 9
  assert solve_2(False) == 1939


print(solve_1(True))
print(solve_1(False))

print(solve_2(True))
print(solve_2(False))