from math import sqrt, prod

# https://adventofcode.com/2023/day/6
with open("06.txt") as file:
    lines = file.readlines()


def get_better_results_count(t, d):
    # speed = hold_time * 1mm
    # distance = speed * (total_race_time - hold_time)
    #          = hold_time * (total_race_time - hold_time)
    # hold_time² - total_race_time * hold_time + track_length = 0
    # => hold_time = t/2 +- sqrt((t/2)² - d)
    # size of the range = end - start + 1
    #                   = t/2 + sqrt((t/2)² - d) - t/2 - sqrt((t/2)² - d) + 1
    #                   = 2 * sqrt((t/2)² - d) + 1
    # for uneven t, adjust the range
    return 2 * int(sqrt((t / 2) ** 2 - d) + 0.5 * (t % 2)) + 1 - (t % 2)


# Part 1
times = [int(t) for t in lines[0].split(":")[1].split()]
distances = [int(d) for d in lines[1].split(":")[1].split()]
better_ways_count = prod(
    get_better_results_count(t, d) for t, d in zip(times, distances)
)
print(f"(Part 1) The solution is {better_ways_count}")  # 293046

# Part 2
t = int(lines[0].split(":")[1].replace(" ", ""))
d = int(lines[1].split(":")[1].replace(" ", ""))
better_ways_count = get_better_results_count(t, d)
print(f"(Part 2) There are {better_ways_count} ways to win the race")  # 35150181
