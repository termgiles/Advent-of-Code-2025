input = open("input", 'r', encoding ="UTF-8").read().strip().split('\n')

def get_neighbours(grid, x, y):
    surrounds = [(i, j) for i in range(-1,2) for j in range(-1,2) if (i, j) != (0, 0)]
    if x == 0:
        surrounds = [coord for coord in surrounds if coord[0] != -1]
    if x == len(grid[y]) -1:
        surrounds = [coord for coord in surrounds if coord[0] != 1]
    if y == 0:
        surrounds = [coord for coord in surrounds if coord[1] != -1]
    if y == len(grid) -1:
        surrounds = [coord for coord in surrounds if coord[1] != 1]

    return [grid[y + s[1]][x + s[0]] for s in surrounds] 

count = 0
for y, l in enumerate(input):
    for x, s in enumerate(l):
        if s == '@':
            if len([item for item in get_neighbours(input, x, y) if item == '@']) < 4:
                count += 1
print(count)

# part 2
grid = [[c for c in l] for l in input]

positive_removes = 1

while positive_removes > 0:
    positive_removes = 0
    for y, l in enumerate(grid):
        for x, s in enumerate(l):
            if s == '@':
                if len([item for item in get_neighbours(grid, x, y) if item == '@']) < 4:
                    grid[y][x] = 'x'
                    positive_removes += 1
print(len([c for l in grid for c in l if c == 'x']))
