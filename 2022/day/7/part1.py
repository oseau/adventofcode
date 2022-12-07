from pathlib import Path


def load():
    with Path(__file__).with_name("input.txt").open("r") as file:
        command_with_results = []
        current = {}
        for l in file:
            l = l.rstrip()
            if l.startswith("$"):
                if current:
                    command_with_results.append(current)
                    current = {}
                if l.startswith("$ cd"):
                    command_with_results.append({"command": l})
                elif l.startswith("$ ls"):
                    current = {"command": l, "results": []}
            else:
                current["results"].append(l)
        if current:
            command_with_results.append(current)
    return command_with_results


def bfs(root, dirs):
    if (size := root.pop("__size")) <= 100000:
        dirs.append(size)
    root.pop("..", None)
    for k, v in root.items():
        bfs(v, dirs)
    return dirs


def main():
    command_with_results = load()
    root = {"__size": 0}
    current = root
    for command_with_result in command_with_results:
        if "results" not in command_with_result:  # cd
            to_folder = command_with_result["command"].split(" ")[2]
            if to_folder not in current:
                current[to_folder] = {"..": current, "__size": 0}
            current = current[to_folder]
        else:  # ls
            for r in command_with_result["results"]:
                if r.startswith("dir "):
                    continue
                addition = int(r.split(" ")[0])
                current_ = current
                while current_:
                    current_["__size"] += addition
                    current_ = current_.get("..", None)
    dirs = bfs(root, [])
    print(sum(dirs))


if __name__ == "__main__":
    main()
