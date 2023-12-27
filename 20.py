from dataclasses import dataclass
from math import lcm

# https://adventofcode.com/2023/day/20
with open("20.txt") as f:
    nodes = f.read().splitlines()


@dataclass
class Node:
    type: str
    targets: list[str]
    activated: bool = False
    inputs_low: dict[str, bool] = None


FLIP_FLOP = "%"
CUNJUNCTION = "&"
BROADCASTER = "broadcaster"


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
    activation_count = {}
    low_pulse_count = high_pulse_count = 0
    while queue:
        name, low, activator = queue.pop(0)
        if low:
            low_pulse_count += 1
        else:
            high_pulse_count += 1
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
            if not signal:
                activation_count[name] = activation_count.get(name, 0) + 1
            for target in node.targets:
                queue.append((target, signal, name))

    return activation_count, low_pulse_count, high_pulse_count


node_before_rx = [node for node in nodes.values() if "rx" in node.targets][0]
interesting_nodes = {name: 0 for name in node_before_rx.inputs_low.keys()}
high_pulse_count = low_pulse_count = 0
for i in range(5000):
    activations, low, high = broadcast()
    if i < 1000:
        low_pulse_count += low
        high_pulse_count += high
    for name, value in interesting_nodes.items():
        if value == 0 and name in activations:
            interesting_nodes[name] = i + 1

print(f"(Part1) low * high = {low_pulse_count * high_pulse_count}")  # 861743850

first_rx_activation = lcm(*list(interesting_nodes.values()))
print(f"(Part2) rx activates after {first_rx_activation} presses")  # 247023644760071
