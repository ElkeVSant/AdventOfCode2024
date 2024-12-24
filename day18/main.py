#! /usr/bin/env python

from heapq import heapify, heappush, heappop
import math


def main():
    positions = []
    with open("day18/input.txt") as byte_positions:
        for pos in byte_positions:
            positions.append(tuple([int(c) for c in pos.split(",")]))
    memory_space = (71, 71)
    memory = [["." for _ in (range(memory_space[0]))] for _ in (range(memory_space[1]))]
    simulate(positions, memory, 1024)
    distances = dijkstra(memory)
    # for line in distances:
    #     print(line)
    mark_path(memory, distances)
    print(len([cell for row in memory for cell in row if cell == "O"]) - 1)
    # print(memory)
    # for line in memory:
    #     print("".join(line))


def simulate(positions: list[tuple[int, int]], memory: list[list[str]], time: int = 1):
    for ns in range(time):
        memory[positions[ns][1]][positions[ns][0]] = "#"
    # for line in memory:
    #     print("".join(line))


def dijkstra(memory: list[list[str]]) -> list[list[float]]:
    distances = [
        [float("inf") if pos == "." else float("nan") for pos in row] for row in memory
    ]
    distances[0][0] = 0
    to_visit = []
    heapify(to_visit)
    heappush(to_visit, (0, 0))
    while len(to_visit):
        pos = heappop(to_visit)
        distance = distances[pos[1]][pos[0]] + 1
        if (
            pos[1] > 0
            and not math.isnan(distances[pos[1] - 1][pos[0]])
            and distances[pos[1] - 1][pos[0]] > distance
        ):
            heappush(to_visit, (pos[0], pos[1] - 1))
            distances[pos[1] - 1][pos[0]] = distance
        if (
            pos[1] < len(distances) - 1
            and not math.isnan(distances[pos[1] + 1][pos[0]])
            and distances[pos[1] + 1][pos[0]] > distance
        ):
            heappush(to_visit, (pos[0], pos[1] + 1))
            distances[pos[1] + 1][pos[0]] = distance
        if (
            pos[0] > 0
            and not math.isnan(distances[pos[1]][pos[0] - 1])
            and distances[pos[1]][pos[0] - 1] > distance
        ):
            heappush(to_visit, (pos[0] - 1, pos[1]))
            distances[pos[1]][pos[0] - 1] = distance
        if (
            pos[0] < len(distances[0]) - 1
            and not math.isnan(distances[pos[1]][pos[0] + 1])
            and distances[pos[1]][pos[0] + 1] > distance
        ):
            heappush(to_visit, (pos[0] + 1, pos[1]))
            distances[pos[1]][pos[0] + 1] = distance
    return distances


def mark_path(memory: list[list[str]], distances: list[list[float]]):
    pos = (len(memory[0]) - 1, len(memory) - 1)
    while pos != (0, 0):
        memory[pos[1]][pos[0]] = "O"
        next = {}
        if (
            pos[1] > 0
            and not math.isnan(distances[pos[1] - 1][pos[0]])
            and memory[pos[1] - 1][pos[0]] != "O"
        ):
            next[(pos[0], pos[1] - 1)] = distances[pos[1] - 1][pos[0]]
        if (
            pos[1] < len(memory[0]) - 1
            and not math.isnan(distances[pos[1] + 1][pos[0]])
            and memory[pos[1] + 1][pos[0]] != "O"
        ):
            next[(pos[0], pos[1] + 1)] = distances[pos[1] + 1][pos[0]]
        if (
            pos[0] > 0
            and not math.isnan(distances[pos[1]][pos[0] - 1])
            and memory[pos[1]][pos[0] - 1] != "O"
        ):
            next[(pos[0] - 1, pos[1])] = distances[pos[1]][pos[0] - 1]
        if (
            pos[0] < len(memory[0]) - 1
            and not math.isnan(distances[pos[1]][pos[0] + 1])
            and memory[pos[1]][pos[0] + 1] != "O"
        ):
            next[(pos[0] + 1, pos[1])] = distances[pos[1]][pos[0] + 1]
        pos = min(next.items(), key=lambda x: x[1])[0]
    memory[pos[1]][pos[0]] = "O"


if __name__ == "__main__":
    main()
