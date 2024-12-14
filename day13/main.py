#! /usr/bin/env python

import re
from sympy import Matrix, linsolve


def main():
    with open("day13/input.txt") as machine_list:
        machine_list = list(machine_list)
        machines = []
        for i in range(0, len(machine_list), 4):
            _, ax, ay = re.split(r"X\+|, Y\+", machine_list[i].rstrip())
            _, bx, by = re.split(r"X\+|, Y\+", machine_list[i + 1].rstrip())
            _, px, py = re.split("X=|, Y=", machine_list[i + 2].rstrip())
            machines.append(
                [(int(ax), int(ay)), (int(bx), int(by)), (int(px), int(py))]
            )
        pushes = []
        for machine in machines:
            pushes.append(calculate_win(machine))
        print(
            sum(
                [
                    3 * a + b
                    for sol, a, b in pushes
                    if sol and 0 <= a <= 100 and 0 <= b <= 100
                ]
            )
        )


def calculate_win(
    machine: list[tuple[int, int]],
) -> tuple[bool, int | None, int | None]:
    M = Matrix([[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]])
    p = Matrix([machine[2][0], machine[2][1]])
    a, b = [sol for sol in linsolve((M, p)).args[0]]  # type: ignore
    if a.is_integer and b.is_integer:
        return True, a, b
    return False, None, None
    # 3*a*ax+ b*bx = px
    # 3*a*ay + b*by = py


if __name__ == "__main__":
    main()
