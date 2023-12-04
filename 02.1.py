# https://adventofcode.com/2023/day/2
with open("02.txt") as file:
    games = file.read().splitlines()

color_maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

valid_sum = 0

for game in games:
    meta, turns = game.split(":")
    game_id = int(meta.split(" ")[1])
    valid = True
    for turn in turns.split(";"):
        for dice in turn.split(","):
            _, count, color = dice.split(" ")
            count = int(count)
            if count > color_maxes[color]:
                valid = False
    if valid:
        valid_sum += game_id

print(f"The sum of all valid Game-Ids is {valid_sum}")  # 2317
