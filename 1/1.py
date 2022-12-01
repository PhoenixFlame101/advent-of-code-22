import sys
from itertools import groupby

lines = list(map(lambda x: x[:-1], sys.stdin.readlines()))
calories_per_elf = list(map(lambda x: sum(map(int, x)), [list(
    sub) for ele, sub in groupby(lines, key=bool) if ele]))


# Part 1
print(max(calories_per_elf))

# Part 2
print(sum(sorted(calories_per_elf, reverse=True)[:3]))
