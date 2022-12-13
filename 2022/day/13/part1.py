import json
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return file.read().strip().split("\n\n")


def is_right_order(left, right):
    if left == right:
        return
    left, right = iter(left), iter(right)
    while True:
        try:
            l = next(left)
        except:
            return True
        try:
            r = next(right)
        except:
            return False
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif l == r:
                continue
            return False
        if not isinstance(l, list):
            l = [l]
        if not isinstance(r, list):
            r = [r]
        if (n := is_right_order(l, r)) is not None:
            return n


def main():
    pairs = load()
    number = total = 0
    for p in pairs:
        number += 1
        first, second = p.split("\n")
        first, second = json.loads(first), json.loads(second)
        if is_right_order(first, second):
            total += number
    print(total)


if __name__ == "__main__":
    main()
