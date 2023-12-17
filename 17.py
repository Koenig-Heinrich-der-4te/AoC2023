import bisect

# https://adventofcode.com/2023/day/17
with open("17.txt") as f:
    city_heat_loss_map = f.read().splitlines()

city_heat_loss_map = [[int(c) for c in row] for row in city_heat_loss_map]

height = len(city_heat_loss_map)
width = len(city_heat_loss_map[0])


# determines the quality of a path, used to sort the queue
def get_order(x, y, cost):
    return cost - ((width - x) + (height - y)) * 5


def inbounds(x, y):
    return 0 <= x < width and 0 <= y < height


def explore(turn_moves, no_turn_moves=0):
    queue = [(get_order(0, 0, 0), 0, 0, (1, 0), 0)]
    explored = {(0, 0, (1, 0)): 0}
    best = 1_000_000_000
    while queue:
        _, x, y, d, cost = queue.pop(0)
        if x == width - 1 and y == height - 1:
            best = min(best, cost)
        # this path is already too expensive
        if cost >= best:
            continue
        # movement before turing is allowed
        for _ in range(no_turn_moves):
            x, y = x + d[0], y + d[1]
            if not inbounds(x, y):
                break
            cost += city_heat_loss_map[y][x]
        # movement after turning is allowed
        for _ in range(turn_moves):
            x, y = x + d[0], y + d[1]
            if not inbounds(x, y):
                break
            cost += city_heat_loss_map[y][x]
            if cost >= best:
                break
            order = get_order(x, y, cost)
            # explore left and right
            for dir in ((-d[1], -d[0]), (d[1], d[0])):
                if (x, y, dir) not in explored or explored[(x, y, dir)] > cost:
                    explored[(x, y, dir)] = cost
                    bisect.insort(queue, (order, x, y, dir, cost))
    return best


large_loss = explore(3)
print(
    f"(Part 1) The smallest heat loss for large crucibles is {large_loss} units"
)  # 1008

ultra_loss = explore(7, 3)
print(
    f"(Part 2) The smallest heat loss for ultra crucibles is {ultra_loss} units"
)  # 1210
