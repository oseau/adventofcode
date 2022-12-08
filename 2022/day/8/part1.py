from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def main():
    lines = load()
    trees = [[int(c) for c in l] for l in lines]
    row = len(trees)
    column = len(trees[0])
    visible = 0
    for i in range(row):
        for j in range(column):
            h = trees[i][j]
            if i == 0 or i == row - 1 or j == 0 or j == column - 1:
                visible += 1
                continue
            if len([0 for i_ in range(i) if trees[i_][j] >= h]) == 0:
                visible += 1
                continue
            if len([0 for i_ in range(i + 1, row) if trees[i_][j] >= h]) == 0:
                visible += 1
                continue
            if len([0 for j_ in range(j) if trees[i][j_] >= h]) == 0:
                visible += 1
                continue
            if len([0 for j_ in range(j + 1, column) if trees[i][j_] >= h]) == 0:
                visible += 1
                continue
    print(visible)


if __name__ == "__main__":
    main()
