# https://adventofcode.com/2023/day/4
with open("04.txt") as file:
    cards = file.read().splitlines()

# {id:amount}
amounts = {}
total_card_count = 0

for card in cards[::-1]:
    meta, content = card.split(": ")
    *_, id = meta.split(" ")
    id = int(id)
    winning_numbers, numbers = [
        [int(num) for num in num_row.split(" ") if len(num) != 0]
        for num_row in content.split(" | ")
    ]

    wins = 0
    for num in numbers:
        if num in winning_numbers:
            wins += 1
    amount = 1
    for copy_id in range(id + 1, id + wins + 1):
        if copy_id in amounts:
            amount += amounts[copy_id]
    amounts[id] = amount
    total_card_count += amount

print(f"You accumulate {total_card_count} scratchcards")  # 9236992
