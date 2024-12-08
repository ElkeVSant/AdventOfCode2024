#! /usr/bin/env python

import copy


def main():
    with open("day6/input.txt") as map:
        map = [list(line.rstrip()) for line in map]
    map, obs = patrol(map)
    print(
        len(map) * len(map[0])
        - [sum(line.count("#") + line.count(".") for line in map)][0]
    )
    print(len(obs))


def patrol(map: list[list[str]]) -> tuple[list[list[str]], set[tuple[str]]]:
    pos = [[i, line.index("^")] for i, line in enumerate(map) if "^" in line][0]
    dir = "^"
    obs = set()
    while pos:
        map, pos, dir = step(map, pos, dir)
        if pos and len(map[pos[0]][pos[1]]) == 2:
            loop = obstruct(map, pos, dir)
            if loop:
                obs.add((pos[0], pos[1]))
    return map, obs


def step(
    map: list[list[str]], pos: list[int], dir: str
) -> tuple[list[list[str]], list[int] | None, str]:
    match dir:
        case "^":
            if pos[0] == 0:
                return map, None, dir
            elif "#" in map[pos[0] - 1][pos[1]]:
                dir = ">"
            else:
                pos[0] -= 1
        case ">":
            if pos[1] == len(map[0]) - 1:
                return map, None, dir
            elif "#" in map[pos[0]][pos[1] + 1]:
                dir = "v"
            else:
                pos[1] += 1
        case "v":
            if pos[0] == len(map) - 1:
                return map, None, dir
            elif "#" in map[pos[0] + 1][pos[1]]:
                dir = "<"
            else:
                pos[0] += 1
        case "<":
            if pos[1] == 0:
                return map, None, dir
            elif "#" in map[pos[0]][pos[1] - 1]:
                dir = "^"
            else:
                pos[1] -= 1
    if map[pos[0]][pos[1]] == dir:
        return map, pos, "loop"
    map[pos[0]][pos[1]] += dir
    return map, pos, dir


def obstruct(map: list[list[str]], pos: list[int], dir: str) -> bool:
    obs_map = copy.deepcopy(map)
    obs_map[pos[0]][pos[1]] = "#"
    obs_pos = None
    obs_dir = None
    match dir:
        case "^":
            obs_pos = [pos[0] + 1, pos[1]]
            obs_dir = ">"
        case ">":
            obs_pos = [pos[0], pos[1] - 1]
            obs_dir = "v"
        case "v":
            obs_pos = [pos[0] - 1, pos[1]]
            obs_dir = "<"
        case "<":
            obs_pos = [pos[0], pos[1] + 1]
            obs_dir = "^"
    check_pos = copy.copy(obs_pos)
    check_dir = obs_dir
    i = 0
    while obs_pos:
        i += 1
        assert obs_dir
        obs_map, obs_pos, obs_dir = step(obs_map, obs_pos, obs_dir)
        if obs_dir == "loop" or (
            obs_pos
            and obs_pos == check_pos
            and check_dir
            and check_dir in obs_map[obs_pos[0]][obs_pos[1]]
            or i == 4 * len(map) * len(map[0])
        ):
            return True
    return False


if __name__ == "__main__":
    main()
