# https://adventofcode.com/2023/day/8
with open("08.txt") as file:
    lines = file.read().splitlines()

instructions = lines[0]
starting_nodes = []
nodes = {}
for line in lines[2:]:
    name = line[0:3]
    nodes[name] = (line[7:10], line[12:15])
    if name[2] == "A":
        starting_nodes.append(name)


def steps_to_Z(node):
    i = 0
    while node[2] != "Z":
        node = nodes[node][instructions[i % len(instructions)] == "R"]
        i += 1
    return i


def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n /= i
            factors.append((i, count))
        i += 1
    return factors


def smallestCommonMultiple(numbers):
    common = []
    for number in numbers:
        factors = prime_factors(number)
        for factor, count in factors:
            elem = [f for f in common if f[0] == factor]
            if len(elem) == 1:
                index = common.index(elem[0])
                count *= elem[0][1]
                common[index] = (factor, count)
            else:
                common.append((factor, count))

    multiple = 1
    for factor, count in common:
        multiple *= factor**count
    return multiple


steps = smallestCommonMultiple(map(steps_to_Z, starting_nodes))
print(
    f"You have to walk {steps} steps to reach Z on all {len(starting_nodes)} paths"
)  # 17099847107071
