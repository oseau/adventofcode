from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        lines = [l.rstrip() for l in file]
    idx = lines.index("")
    return lines[:idx], lines[idx + 1 :]


def main():
    crates, procedures = load()
    indexes = crates.pop()
    stacks_count = int(indexes.split(" ")[-1])
    stacks = [[] for _ in range(stacks_count)]
    for l in reversed(crates):
        for idx, c in enumerate(l):
            if c not in [" ", "[", "]"]:
                stacks[int(indexes[idx]) - 1].append(c)
    for l in procedures:
        splits = l.split(" ")
        count, source, destination = int(splits[1]), int(splits[3]), int(splits[5])
        stacks[destination - 1].extend(stacks[source - 1][-count:])
        stacks[source - 1] = stacks[source - 1][:-count]
    print("".join(s[-1] for s in stacks))


if __name__ == "__main__":
    main()
