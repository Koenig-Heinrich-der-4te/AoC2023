import re

# https://adventofcode.com/2023/day/1
with open("01.txt") as file:
    lines = file.readlines()

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_word_lookup = {word: i + 1 for i, word in enumerate(number_words)}
number = re.compile(
    f"(?=([0-9]|{'|'.join(number_words)}))"
)  # must allow overlapping matches

calibration_sum = 0

for line in lines:
    matches = number.findall(line)

    digit1 = matches[0]
    digit1_value = int(digit1) if len(digit1) == 1 else number_word_lookup[digit1]

    digit2 = matches[-1]
    digit2_value = int(digit2) if len(digit2) == 1 else number_word_lookup[digit2]

    calibration_value = digit1_value * 10 + digit2_value
    calibration_sum += calibration_value

print(f"The sum of all calibration values is {calibration_sum}")  # 54985
