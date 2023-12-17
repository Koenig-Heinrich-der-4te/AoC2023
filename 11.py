# https://adventofcode.com/2023/day/11
with open("11.txt") as file:
    space = file.read().splitlines()


def get_distances(space_multiplier):
    offset = 0
    offset_y = []
    for i in range(len(space)):
        offset_y.append(offset)
        if "#" not in space[i]:
            offset += space_multiplier

    galaxies = []
    offset_x = 0
    for x in range(len(space[0])):
        found_galaxy = False
        for y in range(len(space)):
            if space[y][x] == "#":
                galaxies.append((x + offset_x, y + offset_y[y]))
                found_galaxy = True
        if not found_galaxy:
            offset_x += space_multiplier

    total_distance = 0
    for i, (x, y) in enumerate(galaxies):
        for x2, y2 in galaxies[i + 1 :]:
            distance = abs(x - x2) + abs(y - y2)
            total_distance += distance

    return total_distance


for i, space_multiplier in enumerate((1, 1_000_000 - 1)):
    total_distance = get_distances(space_multiplier)
    print(f"(Part {i+1}) The sum of all distances is {total_distance}")
    # 9686930 & 630728425490
