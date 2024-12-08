#! /usr/bin/env python


def main():
    with open("day6/input.txt") as map:
        map = [line.rstrip() for line in map]
    pos = [[i, line.find("^")] for i, line in enumerate(map) if "^" in line][0]
    map[pos[0]] = map[pos[0]][: pos[1]] + "X" + map[pos[0]][pos[1] + 1 :]
    dir = "^"
    while pos:
        map, pos, dir = patrol(map, pos, dir)
    print(sum([line.count("X") for line in map]))


def patrol(
    map: list[str], pos: list[int], dir: str
) -> tuple[list[str], list[int] | None, str]:
    match dir:
        case "^":
            if pos[0] == 0:
                return map, None, dir
            elif map[pos[0] - 1][pos[1]] == "#":
                return map, pos, ">"
            else:
                pos[0] -= 1
        case ">":
            if pos[1] == len(map[0]) - 1:
                return map, None, dir
            elif map[pos[0]][pos[1] + 1] == "#":
                return map, pos, "v"
            else:
                pos[1] += 1
        case "v":
            if pos[0] == len(map) - 1:
                return map, None, dir
            elif map[pos[0] + 1][pos[1]] == "#":
                return map, pos, "<"
            else:
                pos[0] += 1
        case "<":
            if pos[1] == 0:
                return map, None, dir
            elif map[pos[0]][pos[1] - 1] == "#":
                return map, pos, "^"
            else:
                pos[1] -= 1
    map[pos[0]] = map[pos[0]][: pos[1]] + "X" + map[pos[0]][pos[1] + 1 :]
    return map, pos, dir


if __name__ == "__main__":
    main()
