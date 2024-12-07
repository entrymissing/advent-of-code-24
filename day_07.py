import util
import pytest


def nextOp(ops, curVal, curIdx, result, withConcat=False):
  if curVal > result:
    return False

  if curIdx == len(ops):
    return curVal == result

  addOp = nextOp(ops, curVal + ops[curIdx], curIdx+1, result, withConcat)
  multOp = nextOp(ops, curVal * ops[curIdx], curIdx+1, result, withConcat)
  if withConcat:
    conOp = nextOp(ops, int(str(curVal) + str(ops[curIdx])),
                   curIdx+1, result, withConcat)
    return addOp or multOp or conOp
  else:
    return addOp or multOp


def solve(testing, withConcat=False):
  lines = util.readfile(7, testing)

  calibration = 0
  for line in lines:
    result = int(line.split(':')[0].strip())
    ops = tuple(int(o) for o in line.split(':')[1].split())
    curVal = ops[0]
    curIdx = 1

    if nextOp(ops, curVal, curIdx, result, withConcat):
      calibration += result

  return calibration


def solve_1(testing):
  return solve(testing, False)


def test_solve_1():
  assert solve_1(True) == 3749
  assert solve_1(False) == 1708857123053


def solve_2(testing):
  return solve(testing, True)


def test_solve_2():
  assert solve_2(True) == 11387


@pytest.mark.longrun
def test_solve_2_long():
  assert solve_2(False) == 189207836795655


print(solve_1(True))
print(solve_1(False))
print(solve_2(True))
print(solve_2(False))
