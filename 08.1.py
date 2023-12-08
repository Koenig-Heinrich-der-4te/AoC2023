# https://adventofcode.com/2023/day/8
with open("08.txt") as file:
    lines = file.read().splitlines()

instructions = lines[0]
nodes = {}
for line in lines[2:]:
    nodes[line[0:3]] = (line[7:10], line[12:15])

i = 0
current_node = "AAA"
while current_node != "ZZZ":
    if instructions[i % len(instructions)] == "L":
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]
    i += 1

print(f"{i} steps are required to reach ZZZ")  # 19099
