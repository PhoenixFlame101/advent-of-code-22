import sys
lines = list(map(lambda x: list(map(lambda x: list(
    map(int, x.split('-'))), x[:-1].split(','))), sys.stdin.readlines()))

count1 = 0
count2 = 0
for line in lines:
    overlapping_values = [max(line[0][0], line[1][0]),
                          min(line[0][1], line[1][1])]

    # Part 1
    if overlapping_values in line:
        count1 += 1

    # Part 2
    elif overlapping_values[0] <= overlapping_values[1]:
        count2 += 1

count2 += count1

print(count1)
print(count2)
