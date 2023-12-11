# https://adventofcode.com/2023/day/11
with open("11.txt") as file:
    space = file.read().splitlines()

space_multiplier = 1_000_000 - 1

offset = 0
offset_y = []
for i in range(len(space)):
    offset_y.append(offset)
    if len(set(space[i])) == 1:
        offset += space_multiplier

galaxies = []
offset_x = 0
for x in range(len(space[0])):
    found_galaxy = False
    for y in range(len(space)):
        if space[y][x] == "#":
            galaxies.append((x + offset, y + offset_y[y]))
            found_galaxy = True
    if not found_galaxy:
        offset += space_multiplier

total_distance = 0
for i, (x, y) in enumerate(galaxies):
    for x2, y2 in galaxies[i + 1 :]:
        distance = abs(x - x2) + abs(y - y2)
        total_distance += distance

print(
    f"The sum of the shortest paths between all pairs of galaxies is {total_distance}"  # 630728425490
)
