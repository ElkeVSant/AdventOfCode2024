#! /usr/bin/env python


def main():
    with open("day15/input.txt") as input:
        map, movements = input.read().rstrip().split("\n\n")
    map = [list(row) for row in map.split("\n")]
    movements = movements.replace("\n", "")
    sim_map = simulate_movements(map, movements)
    print(
        sum(
            [
                100 * i + j
                for i in range(len(sim_map))
                for j in range(len(sim_map[0]))
                if sim_map[i][j] == "O"
            ]
        )
    )
    sim_resized_map = simulate_movements(resize(map), movements)
    print(
        sum(
            [
                100 * i + j
                for i in range(len(sim_resized_map))
                for j in range(len(sim_resized_map[0]))
                if sim_resized_map[i][j] == "["
            ]
        )
    )


def simulate_movements(map: list[list[str]], movements: str) -> list[list[str]]:
    sim_map = [row[:] for row in map]
    for m in movements:
        sim_map = attempt_move(sim_map, m)
    return sim_map


def attempt_move(
    map: list[list[str]], m: str, robot: tuple[int, int] | None = None
) -> list[list[str]]:
    map = [row[:] for row in map]
    robot = (
        robot
        if robot
        else [
            (i, j)
            for i, row in enumerate(map)
            for j, char in enumerate(row)
            if char == "@"
        ][0]
    )
    ri = robot[0]
    rj = robot[1]
    match m:
        case "^":
            next = (ri - 1, rj)
        case ">":
            next = (ri, rj + 1)
        case "v":
            next = (ri + 1, rj)
        case _:
            next = (ri, rj - 1)
    if map[next[0]][next[1]] == ".":
        map[next[0]][next[1]] = map[ri][rj]
        map[ri][rj] = "."
    elif map[next[0]][next[1]] == "O" or (
        map[next[0]][next[1]] in ("[", "]") and m in (">", "<")
    ):
        map = attempt_move(map, m, next)
        if map[next[0]][next[1]] == ".":
            map[next[0]][next[1]] = map[ri][rj]
            map[ri][rj] = "."
    elif map[next[0]][next[1]] == "[":
        pot_map = attempt_move(map, m, next)
        if pot_map[next[0]][next[1] + 1] == "]":
            pot_map = attempt_move(pot_map, m, (next[0], next[1] + 1))
        if pot_map[next[0]][next[1]] == "." and pot_map[next[0]][next[1] + 1] == ".":
            map = pot_map
            map[next[0]][next[1]] = map[ri][rj]
            map[ri][rj] = "."
    elif map[next[0]][next[1]] == "]":
        pot_map = attempt_move(map, m, next)
        if pot_map[next[0]][next[1] - 1] == "[":
            pot_map = attempt_move(pot_map, m, (next[0], next[1] - 1))
        if pot_map[next[0]][next[1]] == "." and pot_map[next[0]][next[1] - 1] == ".":
            map = pot_map
            map[next[0]][next[1]] = map[ri][rj]
            map[ri][rj] = "."
    return map


def resize(map: list[list[str]]) -> list[list[str]]:
    new_map = [row[:] for row in map]
    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            match tile:
                case "#":
                    new_map[i].insert(2 * j, "#")
                case "O":
                    new_map[i][2 * j] = "]"
                    new_map[i].insert(2 * j, "[")
                case ".":
                    new_map[i].insert(2 * j, ".")
                case "@":
                    new_map[i].insert(2 * j + 1, ".")
    return new_map


if __name__ == "__main__":
    main()
