from collections import deque
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def main():
    x = 1
    total = 0
    lines = iter(load())
    commands = deque()
    for i in range(1, 220 + 1):
        if i in [20, 60, 100, 140, 180, 220]:
            total += i * x
        if not commands:
            command = next(lines)
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
                x += command
    print(total)


if __name__ == "__main__":
    main()
