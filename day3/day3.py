banks = open("input", 'r', encoding="UTF-8").read().strip().split('\n')
total = 0
for bank in banks:
    bank_list = [int(d) for d in bank]
    index_largest = bank_list.index(max(bank_list[:-1]))
    next_largest = max(bank_list[index_largest + 1:])
    total += int(str(bank_list[index_largest]) + str(next_largest))
print(total)
# part 2

total = 0
for bank in banks:
    bank_list = [int(d) for d in bank]
    digit_sig = 1
    index_largest = bank_list.index(max(bank_list[:-11]))
    jolt_max_str = str(bank_list[index_largest])
    while digit_sig < 11:
        index_largest = index_largest + bank_list[index_largest + 1:].index(max(bank_list[index_largest + 1: - (11 - digit_sig)])) + 1
        jolt_max_str += str(bank_list[index_largest])
        digit_sig += 1
    jolt_max_str += str(max(bank_list[index_largest + 1:]))
    total += int(jolt_max_str)
print(total)
