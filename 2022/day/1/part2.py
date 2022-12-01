from heapq import nlargest
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    return lines


def main():
    lines = load()
    mosts, current = [0, 0, 0], 0
    for l in lines:
        if l:
            current += int(l)
        else:
            mosts = nlargest(3, mosts + [current])
            current = 0
    print(sum(mosts))


if __name__ == "__main__":
    main()
