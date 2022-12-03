from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    total = 0
    lines = load()
    for start in range(0, len(lines), 3):
        a, b, c = lines[start : start + 3]
        for common in set(a) & set(b) & set(c):
            if "a" <= common <= "z":
                total += ord(common) - ord("a") + 1
            else:
                total += ord(common) - ord("A") + 27
    print(total)


if __name__ == "__main__":
    main()
