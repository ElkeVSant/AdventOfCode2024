#! /usr/bin/env python

import re
from math import prod


def main():
    with open("day14/input.txt") as robots:
        pos = []
        vel = []
        for robot in robots:
            _, px, py, vx, vy = re.split(r".{1,2}=|,", robot.rstrip())
            pos.append((int(px), int(py)))
            vel.append((int(vx), int(vy)))
    # room = (11, 7)
    room = (101, 103)
    print(prod(count_quadrants(move(pos, vel, room, 100), room)))

    entropy = 216027840
    for step in range(1, 10000):
        pos = move(pos, vel, room, 1)
        safety_score = prod(count_quadrants(pos, room))
        if safety_score < entropy:
            entropy = safety_score
            _ = display(pos, room)
            print(step)
            print("")


def move(
    pos: list[tuple[int, int]],
    vel: list[tuple[int, int]],
    room: tuple[int, int],
    duration: int,
) -> list[tuple[int, int]]:
    rx = room[0]
    ry = room[1]
    for _ in range(duration):
        new_pos = []
        for i, p in enumerate(pos):
            v = vel[i]
            px = p[0] + v[0]
            if px >= rx:
                px -= rx
            elif px < 0:
                px = rx + px
            py = p[1] + v[1]
            if py >= ry:
                py -= ry
            elif py < 0:
                py = ry + py
            new_pos.append((px, py))
        pos = new_pos
    return pos


def count_quadrants(
    pos: list[tuple[int, int]], room: tuple[int, int]
) -> tuple[int, int, int, int]:
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for p in pos:
        px = p[0]
        py = p[1]
        rx = room[0]
        ry = room[1]
        left = px < rx / 2 - 1
        right = px > rx / 2
        top = py < ry / 2 - 1
        bottom = py > ry / 2
        if top:
            if right:
                q1 += 1
            elif left:
                q2 += 1
        elif bottom:
            if left:
                q3 += 1
            elif right:
                q4 += 1
    return q1, q2, q3, q4


def display(pos: list[tuple[int, int]], room: tuple[int, int]) -> list[str]:
    pattern = [" " * room[0]] * room[1]
    for p in pos:
        px = p[0]
        py = p[1]
        pattern[py] = pattern[py][:px] + "x" + pattern[py][px + 1 :]
    for row in pattern:
        print(row)
    return pattern


if __name__ == "__main__":
    main()
