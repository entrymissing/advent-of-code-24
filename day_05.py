import util
from math import floor
import pytest

def parse_lines(lines):
  rules = []
  pages = []

  is_rule = True
  for line in lines:
    if not line:
      is_rule = False
      continue
    if is_rule:
      a, b = line.split('|')
      rules.append((int(a), int(b)))
    else:
      p = line.split(',')
      pages.append([int(curP) for curP in p])
  return rules, pages

def solve_1(testing):
  lines = util.readfile(5, testing)
  rules, pages = parse_lines(lines)

  sum_of_middle_pages = 0
  for page in pages:
    is_valid_page = True
    for a,b in rules:
      if a not in page or b not in page:
        continue

      if page.index(a) > page.index(b):
        is_valid_page = False
        break
  
    if is_valid_page:
     sum_of_middle_pages += page[floor(len(page)/2)]

  return sum_of_middle_pages

def test_solve_1():
  assert solve_1(True) == 143
  assert solve_1(False) == 5747

def sort_page(page, rules):
  rule_count = {key:0 for key in page}
  for a in page:
    for b in page:
      for rule in rules:
        if rule == (a,b):
          rule_count[a] += 1
  sorted_page = [v[0] for v in sorted(rule_count.items(), key=lambda item: item[1], reverse=True)]
  return sorted_page


def solve_2(testing):
  lines = util.readfile(5, testing)
  rules, pages = parse_lines(lines)

  sum_of_middle_pages = 0
  for page in pages:
    sorted_page = sort_page(page, rules)
    if not sorted_page == page:
      sum_of_middle_pages += sorted_page[floor(len(sorted_page)/2)]
  return sum_of_middle_pages

def test_solve_2():
  assert solve_2(True) == 123

@pytest.mark.longrun
def test_solve_2_long():
  assert solve_2(False) == 5502

print(solve_1(True))
print(solve_1(False))
print(solve_2(True))
print(solve_2(False))
