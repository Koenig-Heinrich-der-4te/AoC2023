from math import lcm

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
    # it's periodic so steps to the first time reaching Z is also the amount of steps to the next time reaching Z
    i = 0
    while node[2] != "Z":
        node = nodes[node][instructions[i % len(instructions)] == "R"]
        i += 1
    return i


steps = lcm(*map(steps_to_Z, starting_nodes))
print(
    f"You have to walk {steps} steps to reach Z on all {len(starting_nodes)} paths"
)  # 17099847107071
