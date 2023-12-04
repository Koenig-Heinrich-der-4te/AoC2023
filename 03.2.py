import re

# https://adventofcode.com/2023/day/3
with open("03.txt") as file:
    schematic = file.read().splitlines()

size_x, size_y = len(schematic[0]), len(schematic)
number = re.compile(r"\d+")
star = re.compile(r"\*")


def find_numbers(y, x):
    numbers = []
    for sy in range(max(y - 1, 0), min(y + 2, size_y)):
        prev_num = 0
        for sx in range(max(x - 1, 0), min(x + 2, size_x)):
            if schematic[sy][sx].isdigit():
                # find start of number
                while sx > 0 and schematic[sy][sx].isdigit():
                    sx -= 1
                num = int(number.search(schematic[sy], sx).group(0))
                if num != prev_num:
                    numbers.append(num)
                    # ignor the number if we find it again
                    prev_num = num
            else:
                prev_num = 0
    return numbers


gear_ratio_sum = 0

for y, line in enumerate(schematic):
    for result in star.finditer(line):
        # find all numbers adjacent to a star
        numbers = find_numbers(y, result.start())
        if len(numbers) == 2:
            part1, part2 = numbers
            gear_ratio = part1 * part2
            gear_ratio_sum += gear_ratio

print(f"The sum of all gear ratios is {gear_ratio_sum}")  # 72246648
