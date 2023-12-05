# https://adventofcode.com/2023/day/5
with open("05.txt") as file:
    lines = file.readlines()


seed_numbers = [int(n) for n in lines[0].split(": ")[1].split()]
seeds = [
    range(seed_numbers[i], seed_numbers[i] + seed_numbers[i + 1])
    for i in range(0, len(seed_numbers), 2)
]


def parse_category(lines, start):
    i = start + 1
    category = []
    while i < len(lines) and len(lines[i]) > 2:
        dest_start, source_start, length = [int(n) for n in lines[i].split()]
        category.append(
            # (start, stop, mapping_offset)
            (source_start, source_start + length, dest_start - source_start)
        )
        i += 1
    return i, category


categorys = []
i = 2
while i < len(lines):
    i, category = parse_category(lines, i)
    categorys.append(category)
    i += 1

ranges = seeds
# map through each category
for category in categorys:
    converted = []
    for unconverted_range in ranges:
        unconverted = [unconverted_range]
        for source_start, source_end, dest_offset in category:
            remaining_unconverted = []
            for r in unconverted:
                if (
                    source_start <= r.start < source_end
                    or source_start < r.stop <= source_end
                    # does r perhaps contain the entire source range?
                    or r.start <= source_start < r.stop
                ):
                    # parts of r outside the source range
                    before = range(r.start, source_start)
                    after = range(source_end, r.stop)
                    if len(before) > 0:
                        remaining_unconverted.append(before)
                    if len(after) > 0:
                        remaining_unconverted.append(after)
                    # part of r in the category's source, mapped to the destination location
                    converted_range = range(
                        max(source_start, r.start) + dest_offset,
                        min(source_end, r.stop) + dest_offset,
                    )
                    if len(converted_range) > 0:
                        converted.append(converted_range)
                else:
                    remaining_unconverted.append(r)  # no collision
            # try processing the remainder with other maps of the category
            unconverted = remaining_unconverted
        converted += unconverted
    ranges = converted


smallest_location_number = min([r.start for r in ranges])
print(
    f"The seed with the closest location is {smallest_location_number} away"
)  # 34039469
