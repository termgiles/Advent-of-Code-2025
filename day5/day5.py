input = open("input", 'r', encoding="UTF-8").read().split("\n\n")
ranges = [[int(line.split('-')[0]), int(line.split('-')[1])] for line in input[0].split('\n')]
ingredients = [int(line) for line in input[1].strip().split('\n')]

fresh = set()
for ing in ingredients:
    for rng in ranges:
        if ing >= rng[0] and ing <= rng[1]:
            fresh.add(ing)
            break
print(len(fresh))

# part 2
o_ranges = sorted(ranges, key = lambda r: r[0])
total = o_ranges[0][1] - o_ranges[0][0] + 1
head = 0
for i, r in enumerate(o_ranges[:-1]):
    head = max(head, r[1])
    if head >= o_ranges[i + 1][0]:
        total += max(o_ranges[i + 1][1] - head, 0)
    else:
        total += o_ranges[i + 1][1] - o_ranges[i + 1][0] + 1
print(total)

