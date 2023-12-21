# https://adventofcode.com/2023/day/21
with open("21.txt") as f:
    garden = f.read()

walkable_count = garden.count(".") + 1
start = garden.find("S")
garden = garden.splitlines()
width = len(garden[0])
height = len(garden)
start = (start % (width + 1), start // (width + 1))


def walk(max_steps):
    queue = [(start, 0)]
    seen = set()
    while queue:
        (x, y), steps = queue.pop(0)
        steps += 1
        if steps > max_steps:
            continue
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if garden[new_y][new_x] == "#":
                continue
            if ((new_x, new_y), steps) in seen:
                continue
            seen.add(((new_x, new_y), steps))
            queue.append(((new_x, new_y), steps))

    return sum(1 for _, steps in seen if steps == max_steps)


accessible_plots = walk(64)
print(f"There are {accessible_plots} plots he could be on after 64 steps.")  # 3795
