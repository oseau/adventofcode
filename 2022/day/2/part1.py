from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    total = 0
    for l in load():
        a, b = l.split(" ")
        total += 1 if b == "X" else 2 if b == "Y" else 3
        diff = ord(b) - ord("X") - (ord(a) - ord("A"))
        total += 3 if diff == 0 else 6 if diff % 3 == 1 else 0
    print(total)


if __name__ == "__main__":
    main()
