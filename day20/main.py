#! /usr/bin/env python


from heapq import heapify, heappush, heappop
import math
# import sys


def main():
    with open("day20/input.txt") as racetrack:
        racetrack = [row.rstrip() for row in racetrack]
    distances, path = dijkstra(racetrack)
    cheats_2_ps = 0
    cheats_20_ps = 0
    for pos in path:
        cheats_2_ps += cheat(pos, distances, 2)
        cheats_20_ps += cheat(pos, distances, 20)
    print(cheats_2_ps)
    print(cheats_20_ps)


def dijkstra(
    racetrack: list[str],
    distances: list[list[float]] | None = None,
    to_visit: list[tuple[int, int]] | None = None,
) -> tuple[list[list[float]], set[tuple[int, int]]]:
    distances = (
        distances
        if distances
        else [
            [float("inf") if pos in [".", "S", "E"] else float("nan") for pos in row]
            for row in racetrack
        ]
    )
    if not to_visit:
        start = [
            (r, c)
            for r, row in enumerate(racetrack)
            if "S" in row
            for c, char in enumerate(row)
            if char == "S"
        ][0]
        distances[start[0]][start[1]] = 0
        to_visit = []
        heapify(to_visit)
        heappush(to_visit, start)
    path = set()
    cheat_options = []
    while len(to_visit):
        pos = heappop(to_visit)
        path.add(pos)
        distance = distances[pos[0]][pos[1]] + 1
        if (
            racetrack[pos[0] - 1][pos[1]] != "#"
            and distances[pos[0] - 1][pos[1]] > distance
        ):
            heappush(to_visit, (pos[0] - 1, pos[1]))
            distances[pos[0] - 1][pos[1]] = distance
        elif pos[0] - 1 > 0 and racetrack[pos[0] - 1][pos[1]] == "#":
            cheat_distances = [row[:] for row in distances]
            cheat_distances[pos[0] - 1][pos[1]] = distance
            cheat_options.append(((pos[0] - 1, pos[1]), pos, distance))
        if (
            racetrack[pos[0] + 1][pos[1]] != "#"
            and distances[pos[0] + 1][pos[1]] > distance
        ):
            heappush(to_visit, (pos[0] + 1, pos[1]))
            distances[pos[0] + 1][pos[1]] = distance
        elif pos[0] + 1 < len(racetrack) - 1 and racetrack[pos[0] + 1][pos[1]] == "#":
            cheat_distances = [row[:] for row in distances]
            cheat_distances[pos[0] + 1][pos[1]] = distance
            cheat_options.append(((pos[0] + 1, pos[1]), pos, distance))
        if (
            racetrack[pos[0]][pos[1] - 1] != "#"
            and distances[pos[0]][pos[1] - 1] > distance
        ):
            heappush(to_visit, (pos[0], pos[1] - 1))
            distances[pos[0]][pos[1] - 1] = distance
        elif pos[1] - 1 > 0 and racetrack[pos[0]][pos[1] - 1] == "#":
            cheat_distances = [row[:] for row in distances]
            cheat_distances[pos[0]][pos[1] - 1] = distance
            cheat_options.append(((pos[0], pos[1] - 1), pos, distance))
        if (
            racetrack[pos[0]][pos[1] + 1] != "#"
            and distances[pos[0]][pos[1] + 1] > distance
        ):
            heappush(to_visit, (pos[0], pos[1] + 1))
            distances[pos[0]][pos[1] + 1] = distance
        elif (
            pos[1] + 1 < len(racetrack[0]) - 1 and racetrack[pos[0]][pos[1] + 1] == "#"
        ):
            cheat_distances = [row[:] for row in distances]
            cheat_distances[pos[0]][pos[1] + 1] = distance
            cheat_options.append(((pos[0], pos[1] + 1), pos, distance))
    return distances, path


def cheat(pos: tuple[int, int], distances: list[list[float]], duration: int) -> int:
    cheats = 0
    for dr in range(-duration, duration + 1):
        row = pos[0] + dr
        if not 1 <= row <= len(distances) - 2:
            continue
        for dc in range(-(duration - abs(dr)), duration - abs(dr) + 1):
            col = pos[1] + dc
            if not 1 <= col <= len(distances[0]) - 2:
                continue
            legal_distance = distances[row][col]
            cheat_distance = distances[pos[0]][pos[1]] + abs(dr) + abs(dc)
            if (
                not math.isnan(legal_distance)
                and legal_distance - cheat_distance >= 100
            ):
                cheats += 1
    return cheats


if __name__ == "__main__":
    main()
