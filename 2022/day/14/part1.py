from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return file.read().strip().split("\n")


def pour(matrix, lowest):
    i, j = 0, 500
    while True:
        if i > lowest:
            return
        elif matrix[i + 1][j] == ".":
            i += 1
        elif matrix[i + 1][j - 1] == ".":
            i += 1
            j -= 1
        elif matrix[i + 1][j + 1] == ".":
            i += 1
            j += 1
        else:
            matrix[i][j] = "o"
            if (i, j) == (0, 500):
                return
            i, j = 0, 500


def main():
    lines = load()
    matrix = [["."] * 600 for _ in range(600)]
    lowest = 0
    for l in lines:
        l = l.split(" -> ")
        for a, b in zip(l, l[1:]):
            (a_j, a_i), (b_j, b_i) = a.split(","), b.split(",")
            a_i, a_j, b_i, b_j = int(a_i), int(a_j), int(b_i), int(b_j)
            if a_i == b_i:
                for j in range(min(a_j, b_j), max(a_j, b_j) + 1):
                    matrix[a_i][j] = "#"
            else:
                for i in range(min(a_i, b_i), max(a_i, b_i) + 1):
                    matrix[i][a_j] = "#"
            lowest = max(lowest, max(a_i, b_i))

    pour(matrix, lowest)
    print(sum([sum(1 for i in l if i == "o") for l in matrix]))


if __name__ == "__main__":
    main()
