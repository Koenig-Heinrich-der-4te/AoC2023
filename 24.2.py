from sympy import symbols, Eq, solve

# https://adventofcode.com/2023/day/24
with open("24.txt") as f:
    hail_stones = f.read().splitlines()

hail_stones = [
    [[int(x) for x in vec.split(", ")] for vec in line.split(" @ ")]
    for line in hail_stones
]

equations = []
t, x0, y0, z0, dx0, dy0, dz0 = symbols("t x0 y0 z0 vx0 vy0 vz0")
for i, ((x, y, z), (dx, dy, dz)) in enumerate(hail_stones[:3]):
    time = solve(Eq(x0 + dx0 * t, x + dx * t), t)[0]
    equations.append(Eq(y0 + dy0 * time, y + dy * time))
    equations.append(Eq(z0 + dz0 * time, z + dz * time))

solution = solve(equations, x0, y0, z0, dx0, dy0, dz0)[0]
print(sum(solution[:3]))  # 769840447420960
