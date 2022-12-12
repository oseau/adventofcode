from collections import deque
from math import inf
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def bfs(start, end, matrix):
    m = len(matrix)
    n = len(matrix[0])
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        (i, j), depth = queue.popleft()
        if (i, j) == end:
            return depth
        current = "a" if (c := matrix[i][j]) == "S" else c
        if (i, j) not in visited:
            visited.add((i, j))
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    target = "z" if (c := matrix[x][y]) == "E" else c
                    if ord(target) <= ord(current) + 1:
                        queue.append(((x, y), depth + 1))
    return -1


def main():
    matrix = [list(l) for l in load()]
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            match c:
                case "S":
                    start = (i, j)
                case "E":
                    end = (i, j)

    print(bfs(start, end, matrix))


if __name__ == "__main__":
    main()
