import util
from collections import defaultdict


def find_senders(map: util.Map):
  senders = defaultdict(list)

  for x in range(map.max_x):
    for y in range(map.max_y):
      if map.get(x, y) != '.':
        senders[map.get(x, y)].append(util.Vector([x, y]))
  return senders


def solve_1(testing: bool):
  lines = util.readfile(8, testing)
  map = util.Map(lines)
  senders = find_senders(map)
  antinodes = []
  for freq in senders:
    locations = senders[freq]
    for i1, loc1 in enumerate(locations):
      for i2, loc2 in enumerate(locations):
        if i1 == i2:
          continue
        antinode = loc1 + ((loc2 - loc1) * 2)
        if map.get(antinode.get_dim(0), antinode.get_dim(1)):
          antinodes.append(antinode)
  print(len(set([a.get() for a in antinodes])))


def solve_2(testing: bool):
  lines = util.readfile(8, testing)
  map = util.Map(lines)
  senders = find_senders(map)
  antinodes = []
  for freq in senders:
    locations = senders[freq]
    for i1, loc1 in enumerate(locations):
      for i2, loc2 in enumerate(locations):
        if i1 == i2:
          continue
        for resonance in range(map.max_x):
          antinode = loc1 + ((loc2 - loc1) * resonance)
          if map.get(antinode.get_dim(0), antinode.get_dim(1)):
            antinodes.append(antinode)
  print(len(set([a.get() for a in antinodes])))


if __name__ == '__main__':
  solve_1(True)
  solve_1(False)
  solve_2(True)
  solve_2(False)
