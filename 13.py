# https://adventofcode.com/2023/day/13
with open("13.txt") as f:
    raw = f.read()


patterns = [pattern.splitlines() for pattern in raw.split("\n\n")]


def row_deviation(pattern, row1, row2):
    return sum(pattern[row1][i] != pattern[row2][i] for i in range(len(pattern[0])))


def column_deviation(pattern, column1, column2):
    return sum(row[column1] != row[column2] for row in pattern)


def check_reflection(pattern, border, center, compare, max_deviation):
    deviation = 0
    for i, j in zip(range(center, -1, -1), range(center + 1, border)):
        deviation += compare(pattern, i, j)
        if deviation > max_deviation:
            return False
    return deviation == max_deviation


def find_reflection(pattern, max_deviation):
    for i in range(len(pattern) - 1):
        if check_reflection(pattern, len(pattern), i, row_deviation, max_deviation):
            return (i + 1) * 100
    for i in range(len(pattern[0]) - 1):
        if check_reflection(
            pattern, len(pattern[0]), i, column_deviation, max_deviation
        ):
            return i + 1


summary = sum(find_reflection(pattern, 0) for pattern in patterns)
summary_corrected = sum(find_reflection(pattern, 1) for pattern in patterns)

print(f"(Part1) The summary of the notes is {summary}")  # 33780
print(f"(Part2) The summary of the corrected notes is {summary_corrected}")  # 23479
