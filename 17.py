import bisect

# https://adventofcode.com/2023/day/17
with open("17.txt") as f:
    city_heat_loss_map = f.read().splitlines()

city_heat_loss_map = [[int(c) for c in row] for row in city_heat_loss_map]

height = len(city_heat_loss_map)
width = len(city_heat_loss_map[0])


def explore(moves, no_turn_moves=0):
    target = (width - 1, height - 1)
    queue = [(0, 0, 0, (1, 0))]
    explored = {(0, 0, (1, 0)): 0}
    best = 1_000_000_000
    while queue:
        cost, x, y, d = queue.pop(0)
        if (x, y) == target:
            best = min(best, cost)
        # this path is already too expensive
        if cost >= best or explored[(x, y, d)] < cost:
            continue
        for i in range(moves):
            x, y = x + d[0], y + d[1]
            if not (0 <= x < width and 0 <= y < height):
                break
            cost += city_heat_loss_map[y][x]
            # check wether we can turn yet
            if i < no_turn_moves:
                continue
            # explore left and right
            for dir in ((-d[1], -d[0]), (d[1], d[0])):
                if (x, y, dir) not in explored or explored[(x, y, dir)] > cost:
                    explored[(x, y, dir)] = cost
                    bisect.insort(queue, (cost, x, y, dir))
    return best


large_loss = explore(3)
print(
    f"(Part 1) The smallest heat loss for large crucibles is {large_loss} units"
)  # 1008

ultra_loss = explore(10, 3)
print(
    f"(Part 2) The smallest heat loss for ultra crucibles is {ultra_loss} units"
)  # 1210
