# https://adventofcode.com/2023/day/11
with open("11.txt") as file:
    space = file.read().splitlines()
offset = 0
for i in range(len(space)):
    if len(set(space[i + offset])) == 1:
        space.insert(i + offset, space[i + offset])
        offset += 1

galaxies = []
offset = 0
for x in range(len(space[0])):
    found_galaxy = False
    for y in range(len(space)):
        if space[y][x] == "#":
            galaxies.append((x + offset, y))
            found_galaxy = True
    if not found_galaxy:
        offset += 1

total_distance = 0
for i, (x, y) in enumerate(galaxies):
    for x2, y2 in galaxies[i + 1 :]:
        distance = abs(x - x2) + abs(y - y2)
        total_distance += distance

print(
    f"The sum of the shortest paths between all pairs of galaxies is {total_distance}"  # 9686930
)
