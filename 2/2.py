import sys

lines = list(map(lambda x: x[:-1].split(), sys.stdin.readlines()))

win_conditions = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw_conditions = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loss_conditions = {'A': 'Z', 'B': 'X', 'C': 'Y'}
rps_scores = {'X': 1, 'Y': 2, 'Z': 3}


# Part 1
score1 = 0
for a, b in lines:
    score1 += rps_scores[b]
    if win_conditions[a] == b:
        score1 += 6
    elif draw_conditions[a] == b:
        score1 += 3

print(score1)


# Part 2
wdl_scores = {'X': 0, 'Y': 3, 'Z': 6}
score2 = 0
for a, b in lines:
    score2 += wdl_scores[b]
    if b == 'Z':
        score2 += rps_scores[win_conditions[a]]
    elif b == 'Y':
        score2 += rps_scores[draw_conditions[a]]
    elif b == 'X':
        score2 += rps_scores[loss_conditions[a]]

print(score2)
