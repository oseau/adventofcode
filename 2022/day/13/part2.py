import json
from functools import cmp_to_key
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [json.loads(l) for l in file.read().split("\n") if l]


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


def cmp(first, second):
    if is_right_order(first, second):
        return -1
    return 1


def main():
    pairs = load() + [[[2]], [[6]]]
    pairs = sorted(pairs, key=cmp_to_key(cmp))
    print((1 + pairs.index([[2]])) * (1 + pairs.index([[6]])))


if __name__ == "__main__":
    main()
