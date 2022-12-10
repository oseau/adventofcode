from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def main():
    lines = load()
    moves = [[m[0], int(m[1])] for l in lines if (m := l.split(" "))]
    length = 10
    knots = [[0, 0] for _ in range(length)]
    tails = set()
    for direction, step in moves:
        for _ in range(step):
            match direction:
                case "U":
                    knots[0][1] += 1
                case "D":
                    knots[0][1] -= 1
                case "L":
                    knots[0][0] -= 1
                case "R":
                    knots[0][0] += 1
            for i in range(1, length):
                if (knots[i - 1][0] - knots[i][0]) ** 2 + (
                    knots[i - 1][1] - knots[i][1]
                ) ** 2 > 2:
                    if knots[i - 1][0] > knots[i][0]:
                        knots[i][0] += 1
                    elif knots[i - 1][0] < knots[i][0]:
                        knots[i][0] -= 1
                    if knots[i - 1][1] > knots[i][1]:
                        knots[i][1] += 1
                    elif knots[i - 1][1] < knots[i][1]:
                        knots[i][1] -= 1
            tails.add(tuple(knots[-1]))
    print(len(tails))


if __name__ == "__main__":
    main()
