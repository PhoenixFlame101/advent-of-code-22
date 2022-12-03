import sys
lines = list(map(lambda x: x[:-1], sys.stdin.readlines()))

def priority(x): return ord(x)-96 if x.islower() else ord(x)-64+26
def grouped(iterable, n): return zip(*[iter(iterable)]*n)

# Part 1
ans1 = 0
for line in lines:
    ans1 += priority(list(set(line[:len(line)//2])
                     & set(line[len(line)//2:]))[0])

print(ans1)

# Part 2
ans2 = 0
for l1, l2, l3 in grouped(lines, 3):
    ans2 += priority(list(set(l1) & set(l2) & set(l3))[0])

print(ans2)
