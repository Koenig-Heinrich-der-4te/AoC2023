# https://adventofcode.com/2023/day/7
with open("07.txt") as file:
    raw_games = file.readlines()


card_values = "23456789TJQKA"

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def get_type_rating(hand):
    distinct_card_count = len(set(hand))
    match distinct_card_count:
        case 1:
            return FIVE_OF_A_KIND
        case 2:
            first_count = hand.count(hand[0])
            if first_count == 4 or first_count == 1:
                return FOUR_OF_A_KIND
            return FULL_HOUSE
        case 3:
            deduplicated = list(set(hand))
            highest_count = max(hand.count(card) for card in deduplicated)
            if highest_count == 3:
                return THREE_OF_A_KIND
            return TWO_PAIR
        case 4:
            return ONE_PAIR
        case 5:
            return HIGH_CARD


# ensures a distinct value for each possible hand
def get_rating(hand):
    rating = get_type_rating(hand)
    for card in hand:
        rating = rating * len(card_values) + card
    return rating


games = []

for raw_game in raw_games:
    hand, reward = raw_game.split()
    hand = [card_values.index(card) for card in hand]
    reward = int(reward)
    games.append((get_rating(hand), reward))

games.sort()

total_winning = 0

for i, game in enumerate(games):
    total_winning += (i + 1) * game[1]

print(f"Your total winnings are {total_winning}")  # 250120186
