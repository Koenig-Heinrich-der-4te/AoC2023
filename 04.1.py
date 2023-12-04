# https://adventofcode.com/2023/day/4
with open("04.txt") as file:
    cards = file.read().splitlines()

total_card_pile_value = 0

for card in cards:
    _, content = card.split(": ")
    winning_numbers, numbers = [
        [int(num) for num in num_row.split(" ") if len(num) != 0]
        for num_row in content.split(" | ")
    ]
    card_value = 0.5
    for num in numbers:
        if num in winning_numbers:
            card_value *= 2
    card_value = int(card_value)
    total_card_pile_value += card_value

print(f"The Pile of cards is worth {total_card_pile_value} points")
