import itertools, math

with open("18.txt") as file:
    instructions = file.read().splitlines()

instructions = [
    [(instr, int(length), color[2:-1]) for instr, length, color in [line.split()]][0]
    for line in instructions
]
default_instructions = [(instr, length) for instr, length, _ in instructions]
color_instructions = [("RDLU"[int(c[5])], int(c[:5], 16)) for *_, c in instructions]

directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
special_corners = ["UL", "UR", "LD", "RD"]


def get_area(instructions):
    pos = (0, 0)
    wall_length = 0
    wall_classify = []
    wall_area = []
    prev = instructions[-1][0]
    for instr, length in instructions:
        wall_length += length
        dir = directions[instr]
        end = (pos[0] + dir[0] * (length - 1), pos[1] + dir[1] * (length - 1))
        # sort into wall areas which are either horizontal or vertical to make it easier to calculate the internal area
        # special corners are treated specially to get the correct area
        if instr in "UD":
            if prev + instr not in special_corners:
                wall_area.append((pos, pos))
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            # start should be higher than end and therefore have the lower y
            wall_classify.append((pos, end) if dir[1] == 1 else (end, pos))
        else:
            if prev + instr in special_corners:
                wall_classify.append((pos, pos))
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            wall_area.append((pos, end))

        pos = (end[0] + dir[0], end[1] + dir[1])
        prev = instr

    return wall_length + get_internal_area(wall_classify, wall_area)


def get_internal_area(wall_classify, wall_area):
    # order by y
    wall_classify.sort(key=lambda x: x[0][1])
    count = 0
    while wall_classify:
        y = wall_classify[0][0][1]
        same_level = [r for r in wall_classify if r[0][1] == y]
        # order by x
        same_level.sort(key=lambda x: x[0][0])
        # wall_classify = wall_classify[len(same_level) :]
        next_lower_y = (
            wall_classify[len(same_level)][0][1]
            if len(wall_classify) > len(same_level)
            else math.inf
        )
        # stop before next lower starts or when the wall ends
        stop_y = min(next_lower_y - 1, min(y for _, (_, y) in same_level))
        y_increment = stop_y - y + 1
        if y_increment <= 0:
            raise Exception("y_increment <= 0")
        for ((ax, _), _), ((bx, _), _) in itertools.batched(same_level, 2):
            # deduct walls inside of the block
            deduction = sum(
                dx - cx + 1
                for (cx, cy), (dx, dy) in wall_area
                if ax < cx < bx and (cy in (y, stop_y) or dy in (y, stop_y))
            )
            # -1 dont count walls
            count += (bx - ax - 1) * y_increment - deduction

        new_start_y = stop_y + 1
        # remove fully accounted for walls and cut of the top, which has already been accounted for
        wall_classify = [
            ((sx, new_start_y), stop)
            for (sx, _), stop in same_level
            if stop[1] >= new_start_y
        ] + wall_classify[len(same_level) :]
    return count


default_area = get_area(default_instructions)
print(f"(Part 1) Area: {default_area}")  # 47045
color_area = get_area(color_instructions)
print(f"(Part 2) Area: {color_area}")  # 147,839,570,293,376
