input = open("input", 'r', encoding ="UTF-8")
input = input.read().strip().split('\n')

# part 1
count = 0
dial = 50

for i in input:
    dial = (dial + (2 * (i[0] == 'R') - 1) * int(i[1:])) % 100
    if dial == 0:
        count += 1

print(count)

# part 2

count = 0
dial = 50

for i in input:
    unmodded_dial = dial + (2 * (i[0] == 'R') -1 ) * int(i[1:])
    if i[0] == 'R':
        count += int(unmodded_dial / 100)
    if unmodded_dial <= 0:
        count += 1 - int(unmodded_dial / 100) - (dial == 0)
    dial = (dial + (2 * (i[0] == 'R') - 1) * int(i[1:])) % 100

print(count)
