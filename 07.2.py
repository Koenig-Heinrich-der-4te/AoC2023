# https://adventofcode.com/2023/day/7
with open("07.txt") as file:
    raw_games = file.readlines()


card_values = "J23456789TQKA"

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def get_type_rating(hand):
    distinct_card_count = len(set(hand))
    if distinct_card_count == 1:
        return FIVE_OF_A_KIND
    if distinct_card_count == 2:
        first_count = hand.count(hand[0])
        if first_count == 4 or first_count == 1:
            return FOUR_OF_A_KIND
        return FULL_HOUSE
    if distinct_card_count == 3:
        deduplicated = list(set(hand))
        highest_count = max(hand.count(card) for card in deduplicated)
        if highest_count == 3:
            return THREE_OF_A_KIND
        return TWO_PAIR
    if distinct_card_count == 4:
        return ONE_PAIR
    return HIGH_CARD


def get_best_type_rating(hand):
    joker_count = hand.count(0)
    if joker_count == 0:
        return get_type_rating(hand)
    # place jokers at the start of the hand for easy replacement
    hand = sorted(hand)
    best_rating = max(
        get_type_rating([replacement_card] * joker_count + hand[joker_count:])
        for replacement_card in set(hand)
    )
    return best_rating


# ensures a distinct value for each possible hand
def get_rating(hand):
    rating = get_best_type_rating(hand)
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

print(f"Your total winnings are {total_winning}")  # 250665248
