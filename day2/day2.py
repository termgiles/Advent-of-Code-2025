input = open("input", 'r', encoding="UTF-8").read().strip().split(',')
ranges = [range(int(line.split('-')[0]), int(line.split('-')[1]) + 1)  for line in input]

def is_repeat(num):
    num_str = str(num)
    if len(num_str) % 2:
        return False
    if num_str[int(len(num_str) / 2):] == num_str[:int(len(num_str) / 2)]:
        return True
    return False

total = 0
for s in ranges:
    for num in s:
        if is_repeat(num):
            total += num
print(total)

# part 2
def factorise(num):
    factors = set([fac for fac in range(1, int((num ** (1/2))) + 1) if num % fac == 0])
    cofactors = [int((num / fac)) for fac in factors if fac != 1]
    factors.update(cofactors)
    return factors

def is_repeats(num):
    num_str = str(num)
    if len(num_str) > 1:
        for fac in factorise(len(num_str)):
            unique_found = 0
            for i in range(1, int((len(num_str) / fac))):
                if num_str[:fac] != num_str[i * fac: (i + 1) * fac]:
                    unique_found += 1
            if not unique_found:
                return True
    return False

total = 0
for s in ranges:
    for num in s:
        if is_repeats(num):
            total += num
print(total)
