from math import sqrt, ceil

# https://adventofcode.com/2023/day/6
with open("06.txt") as file:
    lines = file.readlines()

t = int(lines[0].split(":")[1].replace(" ", ""))
d = int(lines[1].split(":")[1].replace(" ", ""))
# speed = hold_time * 1mm
# distance = speed * (total_race_time - hold_time)
#          = hold_time * (total_race_time - hold_time)
# hold_time² - total_race_time * hold_time + track_length = 0
# => solutions are borders of the range
smallest_beat_hold_time = int((t / 2 - sqrt((t / 2) ** 2 - d)) + 1)
largest_beat_hold_time = int(ceil((t / 2 + sqrt((t / 2) ** 2 - d)) - 1))
beating_ways_count = largest_beat_hold_time - smallest_beat_hold_time + 1

print(f"There are {beating_ways_count} way to win the race")  # 35150181
