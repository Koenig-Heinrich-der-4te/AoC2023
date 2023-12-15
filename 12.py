# https://adventofcode.com/2015/day/12
with open("12.txt") as f:
    lines = f.readlines()


def valid_range(permutation, continueity, until, checker_state):
    hashstreak = 0
    continueity_k, start = checker_state
    next_start = start
    for i in range(start, until):
        if permutation[i] == "#":
            hashstreak += 1
            if hashstreak > continueity[continueity_k]:
                return False, None
        elif hashstreak != 0:
            next_start = i
            if hashstreak != continueity[continueity_k]:
                return False, None
            continueity_k += 1
            hashstreak = 0

    if hashstreak != 0 and until == len(permutation):
        if (
            hashstreak != continueity[continueity_k]
            or continueity_k != len(continueity) - 1
        ):
            return False, None
    return True, (continueity_k, next_start)


default_checker_state = (0, 0)


def permutate_r(
    permutation,
    i,
    continueity,
    hashremain,
    dotremain,
    checker_state=default_checker_state,
):
    key = (i, hashremain, dotremain, checker_state)
    if key in cache:
        return cache[key]
    if hashremain == 0 and dotremain == 0:
        valid, _ = valid_range(
            permutation, continueity, len(permutation), checker_state
        )
        cache[key] = valid
        return valid

    while i < len(permutation) and permutation[i] != "?":
        i += 1
    count = 0

    if hashremain != 0:
        permutation[i] = "#"
        valid, new_checker_state = valid_range(
            permutation, continueity, i + 1, checker_state
        )
        if valid:
            count += permutate_r(
                permutation,
                i + 1,
                continueity,
                hashremain - 1,
                dotremain,
                new_checker_state,
            )

    if dotremain != 0:
        permutation[i] = "."
        valid, new_checker_state = valid_range(
            permutation, continueity, i + 1, checker_state
        )
        if valid:
            count += permutate_r(
                permutation,
                i + 1,
                continueity,
                hashremain,
                dotremain - 1,
                new_checker_state,
            )

    permutation[i] = "?"
    cache[key] = count
    return count


def find_permutations(springs, continueity):
    if springs.count("?") == 0:
        return 1
    parts = springs.split("?")
    working_count = springs.count("#")
    required_working = sum(continueity)
    unkown_working = required_working - working_count
    unkown_not_working = len(parts) - unkown_working - 1
    return permutate_r(
        list(springs), 0, continueity, unkown_working, unkown_not_working
    )


# Part 1
count1 = 0
for line in lines:
    cache = {}
    springs, continueity = line.split()
    continueity = [int(x) for x in continueity.split(",")]
    count1 += find_permutations(springs, continueity)

print(f"(Part1) There are {count1} possible combinations")

# Part 2
count2 = 0
for line in lines:
    cache = {}
    springs, continueity = line.split()
    continueity = [int(x) for x in continueity.split(",")] * 5
    springs = "?".join([springs] * 5)
    count2 += find_permutations(springs, continueity)

print(f"(Part2) There are {count2} possible combinations")
