import time

# https://adventofcode.com/2023/day/23
with open("23.txt") as f:
    hikemap = f.read().splitlines()

goal_y = len(hikemap) - 1
goal_x = len(hikemap[0]) - 2
goal = (goal_x, goal_y)
hikemap = {
    (x, y): c for y, line in enumerate(hikemap) for x, c in enumerate(line) if c != "#"
}
slope_directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def build_hiking_graph(slippery):
    # start heading south
    queue = [((1, 0), (0, 1), (1, 0))]
    graph = {(1, 0): []}
    while queue:
        (x, y), (dx, dy), source = queue.pop()
        length = abs(x - source[0]) + abs(y - source[1])
        while True:
            available_paths = []
            for dir in ((dx, dy), (dy, dx), (-dy, -dx)):
                new_pos = x + dir[0], y + dir[1]
                new_len = length + 1
                if new_pos not in hikemap:
                    continue
                c = hikemap[new_pos]
                # slide over slopes
                if c != ".":
                    new_pos = x + 2 * dir[0], y + 2 * dir[1]
                    new_len += 1
                # take slope direction or current direction if not on slope
                slope = slope_directions.get(c, dir)
                # only go up slopes if not slippery
                if not slippery or slope == dir:
                    available_paths.append((new_pos, dir, new_len))
            # if there are multiple paths, consider this an intersection (which is a node in the graph)
            if len(available_paths) > 1:
                graph[source].append(((x, y), length))
                if (x, y) in graph:
                    break
                graph[(x, y)] = []
                queue.extend(((pos, dir, (x, y)) for pos, dir, _ in available_paths))
                queue.append(((x - dx, y - dy), (-dx, -dy), (x, y)))
                break
            elif len(available_paths) != 0:
                (x, y), (dx, dy), length = available_paths[0]
            else:
                if (x, y) == goal:
                    graph[source].append(((x, y), length))
                break
    return graph


def hike(hiking_graph):
    hikers = [(0, (1, 0), {(1, 0)})]
    longest = 0
    while hikers:
        length, pos, route = hikers.pop()
        if pos == goal:
            longest = max(longest, length)
            continue
        for next_pos, next_len in hiking_graph[pos]:
            if next_pos not in route:
                hikers.append((length + next_len, next_pos, route | {next_pos}))
    return longest


slippery_hiking_graph = build_hiking_graph(True)
most_scenic_slippery_route = hike(slippery_hiking_graph)
print(f"(Part 1) Most scenic route is {most_scenic_slippery_route} tiles long.")  # 2094

print("\nPart 2 is slow, please wait...")
start = time.perf_counter()

hiking_graph = build_hiking_graph(False)
most_scenic_route = hike(hiking_graph)

end = time.perf_counter()
print(f"Part 2 took {end - start:.3f} seconds.\n")

print(f"(Part 2) Most scenic route is {most_scenic_route} tiles long.")  # 6442
