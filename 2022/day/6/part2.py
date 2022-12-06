from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        return [l.rstrip() for l in file][0]


def main():
    line = load()
    for start in range(len(line) - 14 + 1):
        if len(set(line[start : start + 14])) == 14:
            print(line[start : start + 14], start + 14)
            return


if __name__ == "__main__":
    main()
