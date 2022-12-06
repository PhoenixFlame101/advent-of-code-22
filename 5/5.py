import sys
import copy
lines = list(map(lambda x: x[:-1], sys.stdin.readlines()))


def move(stacks, line, crane):
    src, dest, n = -1, -1, 0
    for ele in line.split():
        if ele.isdigit():
            if n == 0:
                n = int(ele)
            elif src == -1:
                src = int(ele)-1
            elif dest == -1:
                dest = int(ele)-1

    eles = stacks[src][-n:]
    stacks[src] = stacks[src][:-n]

    if crane == 9000:
        stacks[dest].extend(eles[::-1])
    elif crane == 9001:
        stacks[dest].extend(eles)
    return stacks


# Parse Stacks
num_stacks = (len(lines[0])+1)//4
stacks = [[] for _ in range(num_stacks)]
for line in lines:
    if '1' in line:
        break
    count = 0
    for i in range(1, len(line)+1, 4):
        if line[i] != ' ':
            stacks[count].insert(0, line[i])
        count += 1

stacks1 = copy.deepcopy(stacks)
stacks2 = copy.deepcopy(stacks)
# Parse move commands
for line in lines:
    if 'move' not in line:
        continue

    # Part 1
    stacks1 = move(stacks1, line, 9000)

    # Part 2
    stacks2 = move(stacks2, line, 9001)


print(''.join([i[-1] for i in stacks1]))
print(''.join([i[-1] for i in stacks2]))
