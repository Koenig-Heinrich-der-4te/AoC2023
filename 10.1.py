# https://adventofcode.com/2023/day/10
with open("10.txt") as file:
    grid = file.read().splitlines()


NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


connections = {
    "|": (NORTH, SOUTH),
    "-": (WEST, EAST),
    "F": (SOUTH, EAST),
    "7": (SOUTH, WEST),
    "J": (NORTH, WEST),
    "L": (NORTH, EAST),
}

opposite = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}


# turns to the next tile and steps to it
def walk(pos, facing):
    x, y = pos
    segment_type = grid[y][x]
    pipe_connections = connections[segment_type]
    # turn to the next tile
    new_facing = (
        pipe_connections[0]
        if pipe_connections[0] != opposite[facing]
        else pipe_connections[1]
    )
    # step to the next tile
    dx, dy = new_facing
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
    dx, dy = direction
    x, y = start_x + dx, start_y + dy
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        if grid[y][x] != "." and opposite[direction] in connections[grid[y][x]]:
            heads.append(((x, y), direction))

walked_steps = 1

# walk until heads meet
while heads[0][0] != heads[1][0]:
    walked_steps += 1
    for i in range(len(heads)):
        heads[i] = walk(*heads[i])

print(f"You have to walk {walked_steps} steps to get the the farthest point.")  # 7086
