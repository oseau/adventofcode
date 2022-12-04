from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    total = 0
    for l in load():
        pair = sorted([[int(s) for s in pair.split("-")] for pair in l.split(",")])
        if pair[1][0] <= pair[0][1]:
            total += 1
    print(total)


if __name__ == "__main__":
    main()
