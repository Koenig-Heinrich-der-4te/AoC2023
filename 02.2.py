# https://adventofcode.com/2023/day/1
with open("02.txt") as file:
    games = file.read().split("\n")

dice_power_sum = 0

for game in games:
    meta, turns = game.split(":")
    game_id = int(meta.split(" ")[1])

    min_dice_count = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for turn in turns.split(";"):
        for dice in turn.split(","):
            _, count, color = dice.split(" ")
            count = int(count)
            if count > min_dice_count[color]:
                min_dice_count[color] = count
    dice_power = (
        min_dice_count["red"] * min_dice_count["green"] * min_dice_count["blue"]
    )
    if dice_power == 0:
        print("Alarm!!")
    dice_power_sum += dice_power

print(f"The sum of all dice powers is {dice_power_sum}")  # 74804
