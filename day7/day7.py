input = open("input", 'r', encoding="UTF-8").read().strip().split('\n')
# part 1

rows = [[int(col == 'S') for col in line] for line in input]
splits = 0

def make_beam(r, splitter_line, i):
    if rows[r - 1][i]:
        if splitter_line[i] == '^':
            if i  < len(splitter_line):
                rows[r][i + 1] += rows[r - 1][i]
            if i > 0:
                rows[r][i - 1] += rows[r -1][i]
            rows[r][i] = 0
            return 1
        rows[r][i] += rows[r -1][i]
    return 0

for j, splitter_line in enumerate(input[1:]):
    r = j + 1
    for i in range(len(splitter_line)):
        splits += make_beam(r, splitter_line, i)

print(splits)
# part 2
print(sum(rows[-1]))
