from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    lines = load()
    most = current = 0
    for l in lines:
        if l:
            current += int(l)
        else:
            most = max(most, current)
            current = 0
    print(most)


if __name__ == "__main__":
    main()
