input = open("input", 'r', encoding="UTF-8").read().strip().split('\n')
junctions = [tuple(map(int,line.split(','))) for line in input]
distances = []

def l2_norm(j1, j2):
    d = ((j1[0] - j2[0]) ** 2 + (j1[1] - j2[1]) ** 2 + (j1[2] - j2[2]) ** 2) ** (1 / 2)
    if d > 0:
        distances.append((j1, j2, d))
    return d

diagrams = {k:sorted(junctions, key = lambda x: l2_norm(k, x)) for k in junctions}
distances.sort(key = lambda d: d[2])
u_distances = set()

for d in distances:
    if d not in u_distances and (d[1], d[0], d[2]) not in u_distances:
        u_distances.add(d)
    if len(u_distances) >= 1000:
        break
circuits = set()

def new_circuit(w, c):
    c.add(w)
    for u in u_distances:
        if u != w and (w[0] in u[:2] or w[1] in u[:2]) and (u not in c):
            new_circuit(u, c)
    return c

for j in u_distances:
    circuits.add(frozenset(new_circuit(j, set())))

def junction_count(c):
    junctions = set()
    for j in c:
        junctions.add(j[0])
        junctions.add(j[1])
    return len(junctions)

circuit_len = sorted([junction_count(c) for c in circuits])
print(circuit_len[-1] * circuit_len[-2] * circuit_len[-3])
# part 2

junctions_set = set(junctions)
cs = [set()]
for d in distances:
    parent_sets = []
    for i, s in enumerate(cs):
        if d[0] in s or d[1] in s:
            parent_sets.append(i)
            s.add(d[0])
            s.add(d[1])
    if len(parent_sets) > 1:
        for j in parent_sets[1:]:
            cs[parent_sets[0]] = cs[parent_sets[0]].union(cs[j])
            cs[j] = set()
        cs = [s for s in cs if s]
    if not parent_sets:
        cs.append(set([d[0], d[1]]))
    if junctions_set in cs:
        print(d[0][0] * d[1][0])
        break

"""
# non-recursive:
def new_circuit(w, c):
    adds = set()
    adds.add(w)

    while adds:
        current = adds.pop()
        for o in u_distances:
            if (o[0] in current[:2] or o[1] in current[:2]) and ( o not in c):
                c.add(o)
                adds.add(o)
    return c
"""
