# https://adventofcode.com/2023/day/24
with open("24.txt") as f:
    hail_stones = f.read().splitlines()

hail_stones = [
    [[int(x) for x in vec.split(", ")] for vec in line.split(" @ ")]
    for line in hail_stones
]
min_bound, max_bound = 200000000000000, 400000000000000
inside_count = 0

for i, ((x, y, z), (dx, dy, dz)) in enumerate(hail_stones):
    for (x2, y2, _), (dx2, dy2, _) in hail_stones[i + 1 :]:
        if (dx2 * dy / dx - dy2) == 0:
            # no collision possible
            continue
        r = (y - y2 - (x - x2) * dy2 / dx2) / (dx * dy2 / dx2 - dy)
        s = (y2 - y - (x2 - x) * dy / dx) / (dx2 * dy / dx - dy2)
        if s < 0 or r < 0:
            # collision is in the past
            continue
        col_x, col_y = x + dx * r, y + dy * r

        if min_bound < col_x < max_bound and min_bound < col_y < max_bound:
            inside_count += 1

print(f"There are {inside_count} intersections in the target area.")  # 16665
