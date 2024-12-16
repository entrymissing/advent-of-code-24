import util
import pickle as pkl
import collections


turn_left = {util.UP: util.LEFT,
             util.RIGHT: util.UP,
             util.DOWN: util.RIGHT,
             util.LEFT: util.DOWN}

turn_right = {util.UP: util.RIGHT,
              util.RIGHT: util.DOWN,
              util.DOWN: util.LEFT,
              util.LEFT: util.UP}


def enqueue_if_visitable(to_visit, visited, pos, d, cost):
  if (pos, d) not in visited:
    visited[(pos, d)] = cost
    to_visit.append((pos, d, cost))
    return True
  if visited[(pos, d)] <= cost:
    return False
  visited[(pos, d)] = cost
  to_visit.append((pos, d, cost))
  return True


def solve_1(testing: bool) -> int:
  lines = util.readfile(16, testing)
  map = util.Map(lines)

  start = util.Vector(map.find_first('S'))
  end = util.Vector(map.find_first('E'))
  min_cost_to_end = None
  visited = dict()

  to_visit = [(start, util.RIGHT, 0)]
  while to_visit:
    pos, d, cost = to_visit.pop()
    if cost > 102000:
      continue

    if min_cost_to_end and cost >= min_cost_to_end:
      continue

    if pos == end:
      min_cost_to_end = cost
      continue

    enqueue_if_visitable(to_visit, visited, pos, turn_left[d], cost + 1000)
    enqueue_if_visitable(to_visit, visited, pos, turn_right[d], cost + 1000)
    if map.get_vector(pos + d) != '#':
      enqueue_if_visitable(to_visit, visited, pos + d, d, cost + 1)

  if testing:
    pkl.dump(visited, open('input/test_16_2.pkl', 'wb+'))
  else:
    pkl.dump(visited, open('input/input_16_2.pkl', 'wb+'))
  return min_cost_to_end


def solve_2(testing: bool) -> int:
  lines = util.readfile(16, testing)
  map = util.Map(lines)

  start = util.Vector(map.find_first('S'))
  end = util.Vector(map.find_first('E'))

  if testing:
    pkl_visited = pkl.load(open('input/test_16_2.pkl', 'rb'))
    goal_value = 7036
  else:
    pkl_visited = pkl.load(open('input/input_16_2.pkl', 'rb'))
    goal_value = 101492

  visited = collections.defaultdict(lambda: (goal_value+1000000))
  for p, d in pkl_visited:
    # if p == util.Vector((4, 7)):
    #   print(p, d, pkl_visited[(p, d)])
    # if p == util.Vector((5, 7)):
    #   print(p, d, pkl_visited[(p, d)])
    visited[p] = min(visited[p], pkl_visited[(p, d)])

  to_visit = [(end, goal_value)]
  spots = set()
  while to_visit:
    pos, val = to_visit.pop()
    spots.add(pos)
    if pos == start:
      continue

    for d in util.MAIN_DIRECTIONS:
      newPos = pos + d
      if newPos in visited:
        if (visited[newPos] == val-1 or visited[newPos] == val-1000
            or visited[newPos] == val-1001):
          to_visit.append((newPos, visited[newPos]))
          continue
      for conDir in util.MAIN_DIRECTIONS:
        if (newPos, conDir) in pkl_visited and (pos, conDir) in pkl_visited:
          if pkl_visited[(newPos, conDir)] == pkl_visited[(pos, conDir)] - 1:
            if newPos not in spots:
              to_visit.append((newPos, visited[newPos]))

  for s in spots:
    map.set_vector(s, 'G')
  print(map)
  return len(spots)


if __name__ == "__main__":
  # print(solve_1(True))
  # print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
