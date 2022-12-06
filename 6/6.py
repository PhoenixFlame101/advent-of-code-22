line = input()


def first_n_unique(line, n):
    first_n_chars = []
    for i, char in enumerate(line):
        first_n_chars.append(char)
        if len(first_n_chars) == n:
            if len(set(first_n_chars)) == n:
                print(i+1)
                break
            first_n_chars.pop(0)


# Part 1
first_n_unique(line, 4)

# Part 2
first_n_unique(line, 14)
