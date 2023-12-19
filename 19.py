import math

# https://adventofcode.com/2023/day/19
with open("19.txt", "r") as f:
    input = f.read()

workflow, parts = input.split("\n\n")
workflows = {}
for line in workflow.splitlines():
    name, workflow_steps = line.split("{")
    workflow_steps = workflow_steps[:-1].split(",")  # strip bracket
    workflow_steps, final_step = workflow_steps[:-1], workflow_steps[-1]
    for i, step in enumerate(workflow_steps):
        condition, instruction = step.split(":")
        condition = (condition[0], condition[1], int(condition[2:]))
        workflow_steps[i] = (instruction, condition)
    workflows[name] = (workflow_steps, final_step)

parts = parts.splitlines()
for i, part in enumerate(parts):
    elements = part[1:-1].split(",")
    parts[i] = {value_part[0]: int(value_part[2:]) for value_part in elements}


def is_valid(workflow_name, value):
    workflow, final_step = workflows[workflow_name]
    for instruction, (cmp_to, cmp, val) in workflow + [(final_step, ("a", ">", -1))]:
        cmp_to = value[cmp_to]
        if cmp == ">" and cmp_to > val or cmp == "<" and cmp_to < val:
            match instruction:
                case "A":
                    return True
                case "R":
                    return False
                case _:
                    return is_valid(instruction, value)


def get_valid_count(workflow_name, values):
    workflow, final_step = workflows[workflow_name]
    count = 0
    for instruction, (cmp_to, cmp, val) in workflow:
        v_cmp_to = values[cmp_to]
        if cmp == ">":
            stop = min(v_cmp_to.stop, val + 1)
            start = min(v_cmp_to.start, stop)
            remainder = range(start, stop)
            inside = range(val + 1, v_cmp_to.stop)
        else:  # <
            start = max(v_cmp_to.start, val)
            stop = max(v_cmp_to.stop, start)
            remainder = range(start, stop)
            inside = range(v_cmp_to.start, val)
        if len(inside) > 0:
            values[cmp_to] = remainder
            match instruction:
                case "A":
                    rest = math.prod(len(v) for k, v in values.items() if k != cmp_to)
                    count += len(inside) * rest
                case "R":
                    pass
                case _:
                    pass_values = values.copy()
                    pass_values[cmp_to] = inside
                    count += get_valid_count(instruction, pass_values)
    match final_step:
        case "A":
            count += math.prod(len(v) for v in values.values())
        case "R":
            pass
        case _:
            count += get_valid_count(final_step, values)
    return count


part1 = sum(sum(part.values()) for part in parts if is_valid("in", part))
print(f"(Part 1) Sum of accepted part ratings: {part1}")  # 480738
part2 = get_valid_count("in", {k: range(1, 4001) for k in "xmas"})
print(f"(Part 2) Number of valid combinations: {part2}")  # 131550418841958
