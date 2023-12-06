from math import sqrt, ceil

# https://adventofcode.com/2023/day/6
with open("06.txt") as file:
    lines = file.readlines()

times = map(int, lines[0].split(":")[1].split())
distances = map(int, lines[1].split(":")[1].split())

result = 1

for t, d in zip(times, distances):
    # speed = hold_time * 1mm
    # distance = speed * (total_race_time - hold_time)
    #          = hold_time * (total_race_time - hold_time)
    # hold_time² - total_race_time * hold_time + track_length = 0
    # => solutions are borders of the range
    smallest_beat_hold_time = int((t / 2 - sqrt((t / 2) ** 2 - d)) + 1)
    largest_beat_hold_time = int(ceil((t / 2 + sqrt((t / 2) ** 2 - d)) - 1))
    print(f"{t}ms, {d}mm : {smallest_beat_hold_time}ms-{largest_beat_hold_time}ms")
    beating_ways_count = largest_beat_hold_time - smallest_beat_hold_time + 1
    result *= beating_ways_count

print(f"The solution is {result}")  # 293046
