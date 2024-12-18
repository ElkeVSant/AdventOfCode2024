#! /usr/bin/env python

import math
from heapq import heapify, heappush, heappop
from dataclasses import dataclass, field
from enum import Enum
from typing import Self


def main():
    with open("day16/input.txt") as map:
        maze = [line.rstrip() for line in map]
    print(
        min(
            [
                dijkstra(maze)[i][row.index("E")]
                for i, row in enumerate(maze)
                if "E" in row
            ][0].values()
        )
    )


class Direction(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"

    def diff(self, other: Self) -> int:
        if self == other:
            return 0
        if {self, other} in [
            {Direction("N"), Direction("S")},
            {Direction("E"), Direction("W")},
        ]:
            return 2000
        return 1000


@dataclass(order=True)
class Node:
    distance: int
    position: tuple[int, int] = field(compare=False)
    direction: Direction = field(compare=False)


def dijkstra(
    maze: list[str],
) -> list[list[dict[Direction, float]]]:
    distances = [
        [
            {
                Direction("N"): float("inf"),
                Direction("E"): float("inf"),
                Direction("S"): float("inf"),
                Direction("W"): float("inf"),
            }
            if loc != "#"
            else {
                Direction("N"): float("nan"),
                Direction("E"): float("nan"),
                Direction("S"): float("nan"),
                Direction("W"): float("nan"),
            }
            for loc in row
        ]
        for row in maze
    ]
    start = Node(
        0,
        [(i, row.index("S")) for i, row in enumerate(maze) if "S" in row][0],
        Direction("E"),
    )
    to_visit = []
    heapify(to_visit)
    heappush(to_visit, start)
    distances[start.position[0]][start.position[1]][start.direction] = 0
    while len(to_visit):
        node = heappop(to_visit)
        if not math.isnan(
            distances[node.position[0] - 1][node.position[1]][Direction("N")]
        ) and distances[node.position[0] - 1][node.position[1]][
            Direction("N")
        ] > node.distance + 1 + node.direction.diff(Direction("N")):
            distances[node.position[0] - 1][node.position[1]][Direction("N")] = (
                node.distance + 1 + node.direction.diff(Direction("N"))
            )
            north = Node(
                distances[node.position[0] - 1][node.position[1]][Direction("N")],
                (node.position[0] - 1, node.position[1]),
                Direction("N"),
            )
            heappush(to_visit, north)
        if not math.isnan(
            distances[node.position[0]][node.position[1] + 1][Direction("E")]
        ) and distances[node.position[0]][node.position[1] + 1][
            Direction("E")
        ] > node.distance + 1 + node.direction.diff(Direction("E")):
            distances[node.position[0]][node.position[1] + 1][Direction("E")] = (
                node.distance + 1 + node.direction.diff(Direction("E"))
            )
            east = Node(
                distances[node.position[0]][node.position[1] + 1][Direction("E")],
                (node.position[0], node.position[1] + 1),
                Direction("E"),
            )
            heappush(to_visit, east)
        if not math.isnan(
            distances[node.position[0] + 1][node.position[1]][Direction("S")]
        ) and distances[node.position[0] + 1][node.position[1]][
            Direction("S")
        ] > node.distance + 1 + node.direction.diff(Direction("S")):
            distances[node.position[0] + 1][node.position[1]][Direction("S")] = (
                node.distance + 1 + node.direction.diff(Direction("S"))
            )
            south = Node(
                distances[node.position[0] + 1][node.position[1]][Direction("S")],
                (node.position[0] + 1, node.position[1]),
                Direction("S"),
            )
            heappush(to_visit, south)
        if not math.isnan(
            distances[node.position[0]][node.position[1] - 1][Direction("W")]
        ) and distances[node.position[0]][node.position[1] - 1][
            Direction("W")
        ] > node.distance + 1 + node.direction.diff(Direction("W")):
            distances[node.position[0]][node.position[1] - 1][Direction("W")] = (
                node.distance + 1 + node.direction.diff(Direction("W"))
            )
            west = Node(
                distances[node.position[0]][node.position[1] - 1][Direction("W")],
                (node.position[0], node.position[1] - 1),
                Direction("W"),
            )
            heappush(to_visit, west)
    return distances


if __name__ == "__main__":
    main()