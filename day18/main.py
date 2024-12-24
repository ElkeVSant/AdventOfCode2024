#! /usr/bin/env python

from heapq import heapify, heappush, heappop
import math


def main():
    positions = []
    with open("day18/input.txt") as byte_positions:
        for pos in byte_positions:
            positions.append(tuple([int(c) for c in pos.split(",")]))
    # memory_space = (7, 7)
    memory_space = (71, 71)
    memory = [["." for _ in (range(memory_space[0]))] for _ in (range(memory_space[1]))]
    original_memory = [row[:] for row in memory]
    # simulate(positions, memory, 12)
    simulate(positions, memory, 1024)
    distances = dijkstra(memory)
    mark_path(memory, distances)
    print(len([cell for row in memory for cell in row if cell == "O"]) - 1)
    print(",".join(str(c) for c in find_blocking_byte(original_memory, positions)))


def simulate(positions: list[tuple[int, int]], memory: list[list[str]], time: int = 1):
    for ns in range(time):
        memory[positions[ns][1]][positions[ns][0]] = "#"


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
        if len(next) == 0:
            return False
        pos = min(next.items(), key=lambda x: x[1])[0]
    memory[pos[1]][pos[0]] = "O"
    return True


def find_blocking_byte(
    memory: list[list[str]], positions: list[tuple[int, int]]
) -> tuple[int, int]:
    for pos in positions:
        simulate([pos], memory)
        distances = dijkstra(memory)
        memory_copy = [row[:] for row in memory]
        if not mark_path(memory_copy, distances):
            return pos
    return (-1, -1)


if __name__ == "__main__":
    main()
