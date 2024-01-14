# https://adventofcode.com/2023/day/22
with open("22.txt") as f:
    bricks = f.read().splitlines()

bricks = [
    [[int(x) for x in end.split(",")] for end in brick.split("~")] + [set()]
    for brick in bricks
]

bricks.sort(key=lambda brick: brick[0][2])
blocked = {}


def move_would_overlap(brick):
    z = brick[0][2] - 1
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if (x, y, z) in blocked:
                return True
    return False


def rests_on(brick):
    bricks = set()
    z = brick[0][2] - 1
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if (x, y, z) in blocked:
                bricks.add(blocked[(x, y, z)])
    return bricks


def settle_brick(brick, id):
    z = brick[1][2]
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            blocked[(x, y, z)] = id


for id, brick in enumerate(bricks):
    while brick[0][2] != 1 and not move_would_overlap(brick):
        brick[0][2] -= 1
        brick[1][2] -= 1
    settle_brick(brick, id)
    resting_on = rests_on(brick)
    for rested_on in resting_on:
        bricks[rested_on][2].add(id)
    brick.append(resting_on)


def get_falling_count(id):
    queue = [id]
    falling = set(queue)
    while queue:
        brick = queue.pop(0)
        for rester in bricks[brick][2]:
            if rester not in falling and bricks[rester][3].issubset(falling):
                falling.add(rester)
                queue.append(rester)
    return len(falling) - 1


moveable_count = 0
for brick in bricks:
    if all(len(bricks[rester][3]) >= 2 for rester in brick[2]):
        moveable_count += 1
print(f"(Part 1) {moveable_count} bricks can be moved safely.")  # 386

falling_count = sum(get_falling_count(id) for id in range(len(bricks)))
print(
    f"(Part 2) In total {falling_count} bricks will fall if one brick is removed."
)  # 39933
