# we're assuming grid is completable here
path = "snake-grid-small.txt"

with open(path) as file:
    lines = file.read().split("\n")

seen = set()

x, y = [int(i) for i in lines[0].split()]
speed_ms = float(lines[1])

grid = [list(line) for line in lines[2:]]

assert grid[x][y] != "."

directions = {
    "r": (1, 0),
    "l": (-1, 0),
    "u": (0, -1),
    "d": (0, 1)
}

time = 1000 # ms
moves = []

while True:
    if (x, y) in seen:
        break

    cell = grid[x][y]
    if cell != ".":
        direction = directions[cell]
        moves.append((
            direction, time
        ))

    seen.add((x, y))

    x += direction[0]
    y += direction[1]

    time += speed_ms

names = {
    (1, 0): "RIGHT",
    (-1, 0): "LEFT",
    (0, 1): "UP",
    (0, -1): "DOWN"
}

output = "snake-win.txt"

press_delay = 10

with open(output, "w") as file:
    for move in moves:
        file.write(f"+[{names[move[0]]}] {move[1] / 1000}\n")
        file.write(f"-[{names[move[0]]}] {(move[1] + press_delay) / 1000}\n")
    file.write(f"@1 {time / 1000}")