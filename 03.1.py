import re

# https://adventofcode.com/2023/day/3
with open("03.txt") as file:
    schematic = file.read().splitlines()

size_x, size_y = len(schematic[0]), len(schematic)
number = re.compile(r"\d+")


def is_symbol(char):
    return not char.isdigit() and char != "."


def find_symbol(y, start, end):
    for sy in range(max(y - 1, 0), min(y + 2, size_y)):
        for sx in range(max(start - 1, 0), min(end + 1, size_x)):
            if is_symbol(schematic[sy][sx]):
                return True
    return False


partnum_sum = 0

for y, line in enumerate(schematic):
    for result in number.finditer(line):
        # the number is a part number if it is adjacent to a symbol (a char that is not a number or a dot)
        if find_symbol(y, *result.span()):
            partnum_sum += int(result.group(0))

print(f"The sum of all part numbers is {partnum_sum}")  # 498559
