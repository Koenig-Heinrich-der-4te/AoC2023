# https://adventofcode.com/2023/day/16
with open("16.txt") as f:
    contrapion = f.read().splitlines()

height = len(contrapion)
width = len(contrapion[0])


N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)


def get_walking_directions(x, y, d):
    match contrapion[y][x]:
        case "|":
            return [N, S]
        case "-":
            return [E, W]
        case "/":
            return [(-d[1], -d[0])]
        case "\\":
            return [(d[1], d[0])]
        case ".":
            return [d]


def seen_tiles_count(start=(0, 0, E)):
    queue = [start]
    explored = set(queue)
    seen = set([start[:2]])
    while queue:
        x, y, d = queue.pop(0)
        for nd in get_walking_directions(x, y, d):
            nx, ny = x + nd[0], y + nd[1]
            if 0 <= nx < width and 0 <= ny < height and (nx, ny, nd) not in explored:
                explored.add((nx, ny, nd))
                seen.add((nx, ny))
                queue.append((nx, ny, nd))
    return len(seen)


print(f"(Part 1) {seen_tiles_count()} tiles will be energized.")  # 7979

print("\nComputing part 2 (this may take a couple seconds)...")
best = 0
for y in range(height):
    best = max(best, seen_tiles_count((0, y, E)), seen_tiles_count((width - 1, y, W)))
for x in range(width):
    best = max(best, seen_tiles_count((x, 0, S)), seen_tiles_count((x, height - 1, N)))

print(f"(Part 2) {best} tiles will be energized from the best starting point.")  # 8437
