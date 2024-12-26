#! /usr/bin/env python


from heapq import heapify, heappush, heappop
import math


def main():
    with open("day20/input.txt") as racetrack:
        racetrack = [row.rstrip() for row in racetrack]
    fastest_time = dijkstra(racetrack)
    # for row in racetrack:
    #     print(row)
    faster_times = 0
    for pos in [
        (r, c)
        for r, row in enumerate(racetrack)
        for c, char in enumerate(row)
        if char == "#" and 0 < r < len(racetrack) - 1 and 0 < c < len(racetrack[0]) - 1
    ]:
        cheat_racetrack = [row for row in racetrack]
        cheat_racetrack[pos[0]] = (
            cheat_racetrack[pos[0]][: pos[1]]
            + "."
            + cheat_racetrack[pos[0]][pos[1] + 1 :]
        )
        # print(dijkstra(cheat_racetrack))
        if fastest_time - dijkstra(cheat_racetrack) >= 100:
            faster_times += 1
    print(faster_times)


def dijkstra(racetrack: list[str]) -> float:
    distances = [
        [float("inf") if pos in [".", "S", "E"] else float("nan") for pos in row]
        for row in racetrack
    ]
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
    while len(to_visit):
        pos = heappop(to_visit)
        distance = distances[pos[0]][pos[1]] + 1
        if (
            not math.isnan(distances[pos[0] - 1][pos[1]])
            and distances[pos[0] - 1][pos[1]] > distance
        ):
            heappush(to_visit, (pos[0] - 1, pos[1]))
            distances[pos[0] - 1][pos[1]] = distance
        if (
            not math.isnan(distances[pos[0] + 1][pos[1]])
            and distances[pos[0] + 1][pos[1]] > distance
        ):
            heappush(to_visit, (pos[0] + 1, pos[1]))
            distances[pos[0] + 1][pos[1]] = distance
        if (
            not math.isnan(distances[pos[0]][pos[1] - 1])
            and distances[pos[0]][pos[1] - 1] > distance
        ):
            heappush(to_visit, (pos[0], pos[1] - 1))
            distances[pos[0]][pos[1] - 1] = distance
        if (
            not math.isnan(distances[pos[0]][pos[1] + 1])
            and distances[pos[0]][pos[1] + 1] > distance
        ):
            heappush(to_visit, (pos[0], pos[1] + 1))
            distances[pos[0]][pos[1] + 1] = distance
    end = [
        (r, c)
        for r, row in enumerate(racetrack)
        if "E" in row
        for c, char in enumerate(row)
        if char == "E"
    ][0]
    return distances[end[0]][end[1]]


if __name__ == "__main__":
    main()
