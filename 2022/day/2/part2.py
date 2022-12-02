from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    total = 0
    for l in load():
        a, b = l.split(" ")
        total += 0 if b == "X" else 3 if b == "Y" else 6
        c = (
            chr(ord("A") + (ord(a) - ord("A") + 2) % 3)
            if b == "X"
            else chr(ord("A") + (ord(a) - ord("A") + 0) % 3)
            if b == "Y"
            else chr(ord("A") + (ord(a) - ord("A") + 1) % 3)
        )
        total += 1 if c == "A" else 2 if c == "B" else 3
    print(total)


if __name__ == "__main__":
    main()
