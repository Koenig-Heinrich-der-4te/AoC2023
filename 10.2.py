# https://adventofcode.com/2023/day/10
with open("10.txt") as file:
    grid = file.read().splitlines()

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

connections = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "F": (EAST, SOUTH),
    "7": (SOUTH, WEST),
    "J": (NORTH, WEST),
    "L": (NORTH, EAST),
}

facing_to_delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def walk(pos, facing):
    x, y = pos
    segment_type = grid[y][x]
    pipe_connections = connections[segment_type]
    new_facing = (
        pipe_connections[0]
        if pipe_connections[0] != ((facing + 2) % 4)
        else pipe_connections[1]
    )
    dx, dy = facing_to_delta[new_facing]
    new_pos = (x + dx, y + dy)
    return (new_pos, new_facing)


heads = []
# find start position
for y, row in enumerate(grid):
    x = row.find("S")
    if x != -1:
        start_pos = (x, y)
        break
start_x, start_y = start_pos
# find start directions
for direction in (NORTH, EAST, SOUTH, WEST):
    dx, dy = facing_to_delta[direction]
    x, y = start_x + dx, start_y + dy
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        if grid[y][x] != "." and ((direction + 2) % 4) in connections[grid[y][x]]:
            heads.append(((x, y), direction))

# substitute start segment with it's actual type
start_dirs = (heads[0][1], heads[1][1])
start_segment = [seg for seg, conn in connections.items() if conn == start_dirs][0]
grid[start_y] = grid[start_y].replace("S", start_segment)

head = heads[0]


loop_map = [[0] * len(grid[0]) for _ in range(len(grid))]

while start_pos != head[0]:
    # mark pipes as part of the loop
    loop_map[head[0][1]][head[0][0]] = 1
    head = walk(*head)
loop_map[head[0][1]][head[0][0]] = 1
count = 0
# count walls encountered while walking left to right, uneven number of walls means we are inside of the loop
for y in range(len(grid)):
    walls = 0
    for x in range(len(grid[0])):
        if loop_map[y][x] == 1:
            segment_type = grid[y][x]
            # "-LJ" are not considered walls because if you offset the ray by 0.25 tiles it wouldnt hit them
            if segment_type not in "-LJ":
                walls += 1
        else:
            if walls % 2 == 1:
                count += 1
print(f"There are {count} tiles inside the loop.")  # 317
