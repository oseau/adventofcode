from collections import deque
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def main():
    register = 1
    lines = iter(load())
    commands = deque()
    screen = [["" for _ in range(40)] for _ in range(6)]
    i = 0
    while True:
        i += 1
        x, y = divmod(i - 1, 40)
        if x == len(screen):
            break
        if register - 1 <= y <= register + 1:
            screen[x][y] = "⬜"
        else:
            screen[x][y] = "⬛"
        if not commands:
            try:
                command = next(lines)
            except:
                break
            if command.startswith("noop"):
                commands.append("noop")
            else:
                command = command.split(" ")
                commands.extend([command[0], int(command[1])])
        command = commands.popleft()
        match command:
            case "noop" | "addx":
                pass
            case _:
                register += command
    for row in screen:
        print("".join(row))


if __name__ == "__main__":
    main()
