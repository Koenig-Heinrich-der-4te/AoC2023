# https://adventofcode.com/2023/day/5
with open("05.txt") as file:
    lines = file.readlines()


class Category:
    def __init__(self, source, destination, ranges):
        self.source = source
        self.destination = destination
        self.ranges = ranges

    def convert(self, n):
        for source, dest_start in self.ranges:
            if n in source:
                return n - source.start + dest_start
        return n


def parse_category(lines, start):
    source, destination = lines[start].split()[0].split("-to-")
    i = start + 1
    ranges = []
    while i < len(lines) and len(lines[i]) > 2:
        dest_start, source_start, length = [int(n) for n in lines[i].split()]
        ranges.append((range(source_start, source_start + length), dest_start))
        i += 1
    return i, Category(source, destination, ranges)


seeds = [int(seed) for seed in lines[0].split(": ")[1].split()]

categorys = []
i = 2

while i < len(lines):
    i, category = parse_category(lines, i)
    categorys.append(category)
    i += 1


def find_location(n):
    for category in categorys:
        n = category.convert(n)
    return n


locations = [find_location(seed) for seed in seeds]
smallest_location_number = min(locations)
print(
    f"The seed with the closest location is {smallest_location_number} away"
)  # 26273516
