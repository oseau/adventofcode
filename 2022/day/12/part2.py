from collections import deque
from math import inf
from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def bfs(start, matrix):
    m = len(matrix)
    n = len(matrix[0])
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        (i, j), depth = queue.popleft()
        if matrix[i][j] in ("a", "S"):
            return depth
        current = "z" if (c := matrix[i][j]) == "E" else c
        if (i, j) not in visited:
            visited.add((i, j))
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    if ord(matrix[x][y]) + 1 >= ord(current):
                        queue.append(((x, y), depth + 1))
    return -1


def main():
    matrix = [list(l) for l in load()]
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            match c:
                case "E":
                    start = (i, j)

    print(bfs(start, matrix))


if __name__ == "__main__":
    main()
