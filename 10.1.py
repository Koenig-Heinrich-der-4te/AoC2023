# https://adventofcode.com/2023/day/10
with open("10.txt") as file:
    grid = file.read().splitlines()


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


connections = {
    "|": (NORTH, SOUTH),
    "-": (WEST, EAST),
    "F": (SOUTH, EAST),
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

walked_steps = 1

while heads[0][0] != heads[1][0] and grid[heads[0][0][1]][heads[0][0][0]] != "S":
    walked_steps += 1
    for i in range(len(heads)):
        heads[i] = walk(*heads[i])

print(f"You have to walk {walked_steps} steps to get the the farthest point.")  # 7086
