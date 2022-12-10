from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def main():
    lines = load()
    moves = [[m[0], int(m[1])] for l in lines if (m := l.split(" "))]
    head, tail = [0, 0], [0, 0]
    tails = set()
    for direction, step in moves:
        for _ in range(step):
            match direction:
                case "U":
                    head[1] += 1
                case "D":
                    head[1] -= 1
                case "L":
                    head[0] -= 1
                case "R":
                    head[0] += 1
            if (head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2 > 2:
                if head[0] > tail[0]:
                    tail[0] += 1
                elif head[0] < tail[0]:
                    tail[0] -= 1
                if head[1] > tail[1]:
                    tail[1] += 1
                elif head[1] < tail[1]:
                    tail[1] -= 1
            tails.add(tuple(tail))
    print(len(tails))


if __name__ == "__main__":
    main()
