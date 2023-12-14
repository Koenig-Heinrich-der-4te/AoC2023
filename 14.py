# https://adventofcode.com/2023/day/14
with open("14.txt") as f:
    platform = f.read().splitlines()

depth = len(platform)
width = len(platform[0])

immovable_rocks = {
    (y, x)
    for y, row in enumerate(platform)
    for x, rock in enumerate(row)
    if rock == "#"
}

rolling_rocks = [
    (y, x)
    for y, row in enumerate(platform)
    for x, rock in enumerate(row)
    if rock == "O"
]


def tilt(tilt_x, tilt_y):
    # put the rocks nearest to the border they will roll to first
    rolling_rocks.sort(
        key=lambda rock: (rock[0] * tilt_y, rock[1] * tilt_x),
        reverse=True,
    )
    stopped_rocks = set()
    for i, (y, x) in enumerate(rolling_rocks):
        while (
            (y, x) not in immovable_rocks
            and (y, x) not in stopped_rocks
            and 0 <= y < depth
            and 0 <= x < width
        ):
            y += tilt_y
            x += tilt_x
        # rocks moved into an invalid position, so move them back
        y -= tilt_y
        x -= tilt_x
        rolling_rocks[i] = (y, x)
        stopped_rocks.add((y, x))
    return stopped_rocks


def cycle():
    for tilt_x, tilt_y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        new_rocks = tilt(tilt_x, tilt_y)
    return new_rocks


def find_repetition():
    previous_states = []
    while True:
        current = cycle()
        if current in previous_states:
            # repeating pattern detected!
            start = previous_states.index(current)
            return start + 1, previous_states[start:]
        previous_states.append(current)


def get_load(stopped_rocks):
    return sum(depth - y for y, x in stopped_rocks)


# Part 1
north_load = get_load(tilt(0, -1))
print(f"Tilting north puts a load of {north_load} on the north support beams")  # 110779

# Part 2
total_cycles = 1_000_000_000
first_cycle, repeating_results = find_repetition()

final_cycle = (total_cycles - first_cycle) % len(repeating_results)

final_cycle_load = get_load(repeating_results[final_cycle])

print(
    f"The sequence repeats every",
    len(repeating_results),
    "cycle(s), starting from cycle",
    first_cycle,
)
print(f"After {total_cycles} cycles, the load is {final_cycle_load}")  # 86069
