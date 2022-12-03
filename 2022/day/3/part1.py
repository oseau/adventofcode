from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    total = 0
    for l in load():
        length = len(l)
        first, second = l[: length // 2], l[length // 2 :]
        for c in set(first) & set(second):
            if "a" <= c <= "z":
                total += ord(c) - ord("a") + 1
            else:
                total += ord(c) - ord("A") + 27
    print(total)


if __name__ == "__main__":
    main()
