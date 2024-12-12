import util


def get_region(map: util.Map, pos: util.Vector) -> set:
  plant = map.get_vector(pos)

  region = set()
  to_visit = set([pos])
  while to_visit:
    curPos = to_visit.pop()
    if curPos in region:
      continue
    if map.get_vector(curPos) == plant:
      region.add(curPos)
      for d in util.MAIN_DIRECTIONS:
        newPos = curPos + d
        if newPos in region:
          continue
        to_visit.add(newPos)
  return region


def calc_circumference(region: set) -> int:
  res = 0
  for spot in region:
    for d in util.MAIN_DIRECTIONS:
      if (spot + d) not in region:
        res += 1
  return res


def find_fences(region: set) -> set:
  fences = set()
  for spot in region:
    for d in util.MAIN_DIRECTIONS:
      if (spot + d) not in region:
        fences.add((spot, d))
  return fences


def find_regions(map: util.Map) -> list:
  visited = set()
  regions = []
  for x in range(map.max_x):
    for y in range(map.max_y):
      pos = util.Vector((x, y))
      if pos in visited:
        continue
      region = get_region(map, util.Vector((x, y)))
      for regionPos in region:
        visited.add(regionPos)
      regions.append(region)
  return regions


orthogonal_dirs = {
  util.Vector((0, 1)): (util.Vector((1, 0)), util.Vector((-1, 0))),
  util.Vector((0, -1)): (util.Vector((1, 0)), util.Vector((-1, 0))),
  util.Vector((1, 0)): (util.Vector((0, 1)), util.Vector((0, -1))),
  util.Vector((-1, 0)): (util.Vector((0, 1)), util.Vector((0, -1))),
}


def merge_fences(fences: list) -> list:
  sides = []
  while fences:
    curPos, curDir = fences.pop()
    curSide = set([curPos])
    to_check = []
    for d in orthogonal_dirs[curDir]:
      to_check.append(curPos + d)
    while to_check:
      newPos = to_check.pop()
      if newPos in curSide:
        continue
      if (newPos, curDir) in fences:
        fences.remove((newPos, curDir))
        curSide.add(newPos)
        for d in orthogonal_dirs[curDir]:
          to_check.append(newPos+d)
    sides.append(curSide)
  return sides


def solve_1(testing: bool) -> int:
  lines = util.readfile(12, testing)
  map = util.Map(lines)

  price = 0
  regions = find_regions(map)
  for region in regions:
    price += len(region) * len(find_fences(region))
  return price


def test_solve_1():
  assert solve_1(True) == 140
  assert solve_1(False) == 1446042


def solve_2(testing: bool) -> int:
  lines = util.readfile(12, testing)
  map = util.Map(lines)

  price = 0
  regions = find_regions(map)
  for region in regions:
    fences = find_fences(region)
    sides = merge_fences(fences)
    price += len(region) * len(sides)

  return price


def test_solve_2():
  assert solve_2(True) == 80
  assert solve_2(False) == 902742


if __name__ == "__main__":
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
