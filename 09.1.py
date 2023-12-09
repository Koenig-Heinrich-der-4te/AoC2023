# https://adventofcode.com/2023/day/9
with open("09.txt") as file:
    lines = file.read().splitlines()

sequences = [[int(n) for n in line.split()] for line in lines]

extrapolated_value_sum = 0

for sequence in sequences:
    table = [sequence]
    while len([0 for t in table[-1] if t != 0]) != 0:
        values = table[-1]
        differences = []
        last_value = values[0]
        for value in values[1:]:
            differences.append(value - last_value)
            last_value = value
        table.append(differences)

    table[-1].append(0)
    for i in range(len(table) - 2, -1, -1):
        differences = table[i + 1]
        values = table[i]
        values.append(values[-1] + differences[-1])
    extrapolated_value_sum += sequence[-1]

print(f"The sum of extrapolated values is {extrapolated_value_sum}")  # 2038472161
