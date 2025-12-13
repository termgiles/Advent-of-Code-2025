input = open("input.txt", 'r', encoding="UTF-8").read()
# part 1

input_p1 = [l.split(' ') for l in input.strip().split('\n')]
cols = [[e for e in l if e != ''] for l in input_p1]
total = 0

for i, symbol in enumerate(cols[-1]):
    if symbol == '+':
        total += sum([int(l[i]) for l in cols[:-1]])
    if symbol == '*':
        prod = 1
        for l in cols[:-1]:
            prod = prod * int(l[i])
        total += prod

print(total)
# part 2

input_p2 = [l for l in input.strip().split('\n')]

def create_num(list, i):
    if i  >= len(list[0]):
        return 0
    num_str = "0"
    for l in list:
        if l[i] not in ('', ' '):
            num_str += l[i]
    return(int(num_str))

total = 0
for i, symbol in enumerate(input_p2[-1]):
    if symbol in ('+', '*'):
        start = create_num(input_p2[:-1], i)
        j = 1
        if symbol == '+':
            while create_num(input_p2[:-1], i + j):
                start += create_num(input_p2, i + j)
                j += 1
        if symbol == '*':
            while create_num(input_p2[:-1], i + j):
                start = start * create_num(input_p2[:-1], i + j)
                j += 1
        total += start

print(total)






