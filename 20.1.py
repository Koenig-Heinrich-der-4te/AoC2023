from dataclasses import dataclass

# https://adventofcode.com/2023/day/20


@dataclass
class Node:
    type: str
    targets: list[str]
    activated: bool = False
    inputs_low: dict[str, bool] = None


FLIP_FLOP = "%"
CUNJUNCTION = "&"
BROADCASTER = "broadcaster"

with open("20.txt") as f:
    nodes = f.read().splitlines()

nodes = {
    name[1:] if name != BROADCASTER else BROADCASTER: Node(name[0], targets.split(", "))
    for name, targets in (node.split(" -> ") for node in nodes)
}

# link inputs to outputs
for name, node in nodes.items():
    node.inputs_low = {
        input_name: True
        for input_name, input_node in nodes.items()
        if name in input_node.targets
    }


def broadcast():
    queue = [(BROADCASTER, True, None)]
    activation_count = {True: 0, False: 0}
    while queue:
        name, low, activator = queue.pop(0)
        activation_count[low] += 1
        if name not in nodes:
            continue
        node = nodes[name]
        signal = None
        if name == BROADCASTER:
            signal = low
        elif node.type == FLIP_FLOP:
            if low:
                signal = node.activated
                node.activated = not node.activated
        elif node.type == CUNJUNCTION:
            node.inputs_low[activator] = low
            all_high = not any(node.inputs_low.values())
            signal = all_high
        if signal is not None:
            for target in node.targets:
                queue.append((target, signal, name))

    return activation_count


activation_count = {True: 0, False: 0}
for i in range(1000):
    activation_count = {k: v + activation_count[k] for k, v in broadcast().items()}

print(activation_count[True] * activation_count[False])  # 861743850
