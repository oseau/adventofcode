from collections import deque
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.strip() for l in file]


def main():
    lines = load()
    monkeys = []
    for l in lines:
        if not l:
            continue
        if l.startswith("Monkey "):
            monkeys.append({"times": 0})
        elif l.startswith("Starting items: "):
            monkeys[-1]["items"] = deque(
                [int(i) for i in l.lstrip("Starting items: ").split(", ")]
            )
        elif l.startswith("Operation: new = old "):
            l = l.lstrip("Operation: new = old ").split(" ")
            monkeys[-1]["operation"] = l
        elif l.startswith("Test: divisible by "):
            monkeys[-1]["div"] = int(l.lstrip("Test: divisible by "))
        elif l.startswith("If true: throw to monkey "):
            monkeys[-1][True] = int(l.lstrip("If true: throw to monkey "))
        elif l.startswith("If false: throw to monkey "):
            monkeys[-1][False] = int(l.lstrip("If false: throw to monkey "))

    divs = 1
    for m in monkeys:
        divs *= m["div"]
    for _ in range(10000):
        for m in monkeys:
            while m["items"]:
                i = m["items"].popleft()
                operation = i if (o := m["operation"][1]) == "old" else int(o)
                match m["operation"][0]:
                    case "+":
                        after = i + operation
                    case "-":
                        after = i - operation
                    case "*":
                        after = i * operation
                    case "/":
                        after = i // operation
                div = after % divs
                monkeys[m[not (div % m["div"])]]["items"].append(div)
                m["times"] += 1
    a, b, *_ = sorted([m["times"] for m in monkeys], reverse=True)
    print(a * b)


if __name__ == "__main__":
    main()
