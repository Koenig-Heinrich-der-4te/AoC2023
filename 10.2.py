# https://adventofcode.com/2023/day/10
with open("10.txt") as file:
    grid = file.read().splitlines()

width = len(grid[0])
height = len(grid)

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)

connections = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "F": (EAST, SOUTH),
    "7": (SOUTH, WEST),
    "J": (NORTH, WEST),
    "L": (NORTH, EAST),
}

opposite = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}


def walk(pos, facing):
    x, y = pos
    segment_type = grid[y][x]
    pipe_connections = connections[segment_type]
    new_facing = (
        pipe_connections[0]
        if pipe_connections[0] != opposite[facing]
        else pipe_connections[1]
    )
    dx, dy = new_facing
    new_pos = (x + dx, y + dy)
    return (new_pos, new_facing)


heads = []
# find start position
for y, row in enumerate(grid):
    if "S" in row:
        start_pos = (row.find("S"), y)
        break
start_x, start_y = start_pos

# find start directions
for direction in (NORTH, EAST, SOUTH, WEST):
    dx, dy = direction
    x, y = start_x + dx, start_y + dy
    if 0 <= x < width and 0 <= y < height:
        tile = grid[y][x]
        if tile != "." and opposite[direction] in connections[tile]:
            heads.append(((x, y), direction))

# substitute start segment with it's actual type
start_dirs = (heads[0][1], heads[1][1])
start_segment = [seg for seg, conn in connections.items() if conn == start_dirs][0]
grid[start_y] = grid[start_y].replace("S", start_segment)

head = heads[0]


loop_map = [[0] * width for _ in range(height)]

while start_pos != head[0]:
    # mark pipes as part of the loop
    x, y = head[0]
    loop_map[y][x] = 1

    head = walk(*head)

x, y = head[0]
loop_map[y][x] = 1

count = 0
# count walls encountered while walking left to right, uneven number of walls means we are inside of the loop
for y in range(height):
    walls = 0
    for x in range(width):
        if loop_map[y][x] == 1:
            segment_type = grid[y][x]
            # "-LJ" are not considered walls because if you offset the ray by 0.25 tiles it wouldnt hit them
            if segment_type not in "-LJ":
                walls += 1
        elif walls % 2 == 1:
            count += 1

print(f"There are {count} tiles inside the loop.")  # 317
