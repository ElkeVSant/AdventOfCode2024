#! /usr/bin/env python


def main():
    with open("day15/input.txt") as input:
        map, movements = input.read().rstrip().split("\n\n")
    map = [list(row) for row in map.split("\n")]
    movements = movements.replace("\n", "")
    map = simulate_movements(map, movements)
    print(
        sum(
            [
                100 * i + j
                for i in range(len(map))
                for j in range(len(map[0]))
                if map[i][j] == "O"
            ]
        )
    )


def simulate_movements(map: list[list[str]], movements: str) -> list[list[str]]:
    for i, m in enumerate(movements):
        map = attempt_move(map, m)
    return map


def attempt_move(
    map: list[list[str]], m: str, robot: tuple[int, int] | None = None
) -> list[list[str]]:
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
    elif map[next[0]][next[1]] == "O":
        map = attempt_move(map, m, next)
        if map[next[0]][next[1]] == ".":
            map[next[0]][next[1]] = map[ri][rj]
            map[ri][rj] = "."
    return map


if __name__ == "__main__":
    main()
