# https://adventofcode.com/2023/day/21
with open("21.txt") as f:
    garden = f.read()

walkable_count = garden.count(".") + 1
start = garden.find("S")
garden = garden.splitlines()
width = len(garden[0])
height = len(garden)
start = (start % (width + 1), start // (width + 1))


def walk(start, max_steps):
    queue = [(start, 0)]
    seen = set(queue)
    while queue:
        (x, y), steps = queue.pop(0)
        steps += 1
        if steps > max_steps:
            continue
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if not (0 <= new_x < width and 0 <= new_y < height):
                continue
            if garden[new_y][new_x] == "#":
                continue
            if ((new_x, new_y), steps % 2) in seen:
                continue
            seen.add(((new_x, new_y), steps % 2))
            queue.append(((new_x, new_y), steps))

    return sum(1 for _, steps in seen if steps == max_steps % 2)


# Part 1
accessible_plots = walk(start, 64)
print(
    f"(Part 1) There are {accessible_plots} plots he could reach with exactly 64 steps."
)  # 3795

# Part 2
# distances sutff, assume corridors going in all directions from the center
total_steps = 26501365
border_steps_remain = total_steps - start[0]
radius = border_steps_remain // width
# manhattan distance whatever
a_count = (radius + radius % 2 - 1) ** 2
b_count = (radius - radius % 2) ** 2
atile = walk(start, 2 * width + total_steps % 2)
btile = walk(start, 2 * width + total_steps % 2 + 1)
inner_count = a_count * atile + b_count * btile
# outer layer
# corners
steps_remain = border_steps_remain - width * (radius - 1) - 1
outer_count = 0
for start_pos in (
    (width - 1, start[1]),
    (0, start[1]),
    (start[0], height - 1),
    (start[0], 0),
):
    outer_count += walk(start_pos, steps_remain)
# sides
side_length_outer = radius
side_length_inner = radius - 1
side_steps_remain_outer = steps_remain - start[0] - 1
side_steps_remain_inner = side_steps_remain_outer + width
for side_start in ((width - 1, 0), (width - 1, height - 1), (0, 0), (0, height - 1)):
    outer_count += walk(side_start, side_steps_remain_outer) * side_length_outer
    outer_count += walk(side_start, side_steps_remain_inner) * side_length_inner
total = outer_count + inner_count
print(
    f"(Part 2) There are {total} plots he could reach with exactly {total_steps} steps."
)  # 630129824772393
