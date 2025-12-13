f = open("./input", "r", encoding="UTF-8")
input = f.read().strip().split('\n')

start = 50
count = 0
for i in input:
    start = (start + (2*(i[0] == 'R') -1) * int(i[1:])) % 100
    if start == 0:
        count += 1

print(count)

# part2
