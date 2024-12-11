import util
import pytest


def read_sequence(line):
  seqs = []
  curStart = 0
  isBlank = False
  for idx, val in enumerate(line):
    if val == 0:
      isBlank = not isBlank
      continue
    if isBlank:
      seqs.append([curStart, val, '.'])
    else:
      seqs.append([curStart, val, int(idx/2)])
    isBlank = not isBlank
    curStart += val
  return seqs


def find_first_blank(seqs):
  for idx, seq in enumerate(seqs):
    if seq[2] == '.':
      return idx, seq
  return None, None


def find_last_seq(seqs):
  for idx, seq in enumerate(reversed(seqs)):
    if seq[2] != '.':
      return len(seqs)-idx-1, seq
  return None, None


def defrag_seq(seqs: list, from_idx, from_val, to_idx, to_val):
  if from_val[1] >= to_val[1]:
    seqs[to_idx][2] = seqs[from_idx][2]
    seqs[from_idx][1] = seqs[from_idx][1] - seqs[to_idx][1]
    if seqs[from_idx][1] == 0:
      del seqs[from_idx]
  else:
    seqs[to_idx][1] = seqs[to_idx][1] - seqs[from_idx][1]
    seqs.insert(to_idx, from_val)
    del seqs[from_idx+1]


def print_seq(seqs, output=True):
  res = ''
  for seq in seqs:
    for _ in range(seq[1]):
      res += str(seq[2])
  if output:
    print(res)
  return res


def calc_checksum(seqs):
  res = 0
  idx = 0
  for seq in seqs:
    for _ in range(seq[1]):
      if isinstance(seq[2], int):
        res += seq[2] * idx
      idx += 1
  return res


def solve_1(testing: bool):
  line = util.readfile(9, testing)[0]
  line = [int(v) for v in line]
  seqs = read_sequence(line)

  to_idx, to_val = find_first_blank(seqs)
  while to_val:
    from_idx, from_val = find_last_seq(seqs)
    defrag_seq(seqs, from_idx, from_val, to_idx, to_val)
    to_idx, to_val = find_first_blank(seqs)
  return calc_checksum(seqs)


def test_solve_1():
  assert solve_1(True) == 1928


def find_next_seq_to_move(seqs: list, file_number: int):
  for idx in range(len(seqs)-1, 0, -1):
    if seqs[idx][2] == file_number:
      return idx, seqs[idx]
  return None, None


def move_seq_if_possible(seqs: list, from_idx: int, from_val: list):
  for to_idx, to_val in enumerate(seqs):
    if to_val[2] != '.':
      continue

    if to_idx >= from_idx:
      break

    if to_val[1] < from_val[1]:
      continue

    seqs[to_idx][1] = seqs[to_idx][1] - seqs[from_idx][1]
    seqs.insert(to_idx, from_val.copy())
    seqs[from_idx+1][2] = '.'
    break


def solve_2(testing: bool):
  line = util.readfile(9, testing)[0]
  line = [int(v) for v in line]
  seqs = read_sequence(line)

  file_number = seqs[-1][2]
  while True:
    from_idx, from_val = find_next_seq_to_move(seqs, file_number)
    file_number -= 1
    if not from_val:
      break
    move_seq_if_possible(seqs, from_idx, from_val)
  return calc_checksum(seqs)


def test_solve_2():
  assert solve_2(True) == 2858


@pytest.mark.longrun
def test_solve_long():
  assert solve_1(False) == 6359213660505
  assert solve_2(False) == 6381624803796


if __name__ == '__main__':
  print(solve_1(True))
  print(solve_1(False))
  print(solve_2(True))
  print(solve_2(False))
