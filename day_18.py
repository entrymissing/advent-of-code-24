import util
import heapq


def solve_1(testing: bool) -> int:
  lines = util.readfile(18, testing)

  if testing:
    map_size = 7
    num_blocks = 12
  else:
    map_size = 71
    num_blocks = 1024

  map_lines = []
  for x in range(map_size):
    map_lines.append('.' * map_size)

  map = util.Map(map_lines)
  for line in lines[:num_blocks]:
    x, y = line.split(',')
    map.set(int(x), int(y), '#')

  start = util.Vector((0, 0))
  goal = util.Vector((map_size - 1, map_size - 1))
  to_visit = [(0, start)]
  heapq.heapify(to_visit)
  cost_map = {start: 0}

  while len(to_visit):
    cost, curPos = heapq.heappop(to_visit)
    for d in util.MAIN_DIRECTIONS:
      nextPos = curPos + d
      if map.get_vector(nextPos) != '.':
        continue

      if nextPos not in cost_map or cost_map[nextPos] > cost + 1:
        heapq.heappush(to_visit, (cost + 1, nextPos))
        cost_map[nextPos] = cost + 1
  return cost_map[goal]


def solve_2(testing: bool) -> int:
  lines = util.readfile(18, testing)

  if testing:
    map_size = 7
    num_blocks = 12
  else:
    map_size = 71
    num_blocks = 1024

  for num_blocks in range(num_blocks, len(lines)):
    map_lines = []
    for x in range(map_size):
      map_lines.append('.' * map_size)

    map = util.Map(map_lines)
    for line in lines[:num_blocks]:
      x, y = line.split(',')
      map.set(int(x), int(y), '#')
    last_added = lines[num_blocks-1]

    start = util.Vector((0, 0))
    goal = util.Vector((map_size - 1, map_size - 1))
    to_visit = [(0, start)]
    heapq.heapify(to_visit)
    cost_map = {start: 0}

    while len(to_visit):
      cost, curPos = heapq.heappop(to_visit)
      for d in util.MAIN_DIRECTIONS:
        nextPos = curPos + d
        if map.get_vector(nextPos) != '.':
          continue

        if nextPos not in cost_map or cost_map[nextPos] > cost + 1:
          heapq.heappush(to_visit, (cost + 1, nextPos))
          cost_map[nextPos] = cost + 1
    if goal not in cost_map:
      return last_added


if __name__ == "__main__":
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
