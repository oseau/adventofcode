from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file]


def main():
    lines = load()
    trees = [[int(c) for c in l] for l in lines]
    row = len(trees)
    column = len(trees[0])
    scenic_score_max = 0
    for i in range(row):
        for j in range(column):
            h = trees[i][j]
            up = down = left = right = 0
            i_ = i - 1
            while i_ >= 0:
                up += 1
                if trees[i_][j] >= h:
                    break
                i_ -= 1
            i_ = i + 1
            while i_ < row:
                down += 1
                if trees[i_][j] >= h:
                    break
                i_ += 1
            j_ = j - 1
            while j_ >= 0:
                left += 1
                if trees[i][j_] >= h:
                    break
                j_ -= 1
            j_ = j + 1
            while j_ < column:
                right += 1
                if trees[i][j_] >= h:
                    break
                j_ += 1
            scenic_score_max = max(scenic_score_max, up * down * left * right)
    print(scenic_score_max)


if __name__ == "__main__":
    main()
