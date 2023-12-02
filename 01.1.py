import re

# https://adventofcode.com/2023/day/1
with open("01.txt") as file:
    lines = file.readlines()

number = re.compile(r"[0-9]")

calibration_sum = 0

for line in lines:
    matches = number.findall(line)
    digit1 = matches[0]
    digit2 = matches[-1]
    calibration_value = int(digit1 + digit2)
    calibration_sum += calibration_value

print(f"The sum of all calibration values is {calibration_sum}")  # 55130
