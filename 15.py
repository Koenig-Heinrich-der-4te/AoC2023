import re

# https://adventofcode.com/2023/day/15
with open("15.txt") as f:
    steps = f.read().split(",")


def hash(step: str):
    value = 0
    for c in step:
        value = (value + ord(c)) * 17 % 256
    return value


HASHMAP = [[] for _ in range(256)]


def process_step(step):
    label = re.match(r"[a-z]+", step).group(0)
    box = hash(label)
    if step.endswith("-"):
        HASHMAP[box] = [slot for slot in HASHMAP[box] if slot[0] != label]
        return
    lense = int(step[-1])
    HASHMAP[box] = [
        slot if slot[0] != label else (label, lense) for slot in HASHMAP[box]
    ]
    if (label, lense) not in HASHMAP[box]:
        HASHMAP[box].append((label, lense))


def get_focussing_power():
    return sum(
        sum(lense * (i + 1) for i, (_, lense) in enumerate(slots)) * (j + 1)
        for j, slots in enumerate(HASHMAP)
    )


hash_sum = 0
for step in steps:
    hash_sum += hash(step)
    process_step(step)

print(f"(Part 1) The hash sum is {hash_sum}")  # 510801

foccussing_power = get_focussing_power()

print(f"(Part 2) The focussing power is {foccussing_power}")  # 212763
