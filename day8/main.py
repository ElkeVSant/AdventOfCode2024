#! /usr/bin/env python

from collections import defaultdict
from itertools import combinations, permutations


def main():
    with open("day8/input.txt") as map:
        map = [[*line.rstrip()] for line in map]
    print(len(find_antinodes(map)))
    print(len(find_resonant_antinodes(map)))


def find_frequencies(map: list[list[str]]) -> defaultdict[str, list[tuple[int, int]]]:
    frequencies = defaultdict(list)
    for i, line in enumerate(map):
        for j, freq in enumerate(line):
            if freq != ".":
                frequencies[freq].append((i, j))
    return frequencies


def find_antinodes(map: list[list[str]]) -> set[tuple[int, int]]:
    frequencies = find_frequencies(map)
    antinodes = set()
    height = len(map)
    width = len(map[0])
    for freq in frequencies:
        for comb in combinations(frequencies[freq], 2):
            for perm in permutations(comb):
                a = perm[0][0]
                b = perm[0][1]
                c = perm[1][0]
                d = perm[1][1]
                if (
                    (row := a + (a - c)) >= 0
                    and row < height
                    and (col := b + (b - d)) >= 0
                    and col < width
                ):
                    antinodes.add((row, col))
    return antinodes


def find_resonant_antinodes(map: list[list[str]]) -> set[tuple[int, int]]:
    frequencies = find_frequencies(map)
    antinodes = set()
    height = len(map)
    width = len(map[0])
    for freq in frequencies:
        for comb in combinations(frequencies[freq], 2):
            antinodes.add(comb[0])
            antinodes.add(comb[1])
            for perm in permutations(comb):
                a = perm[0][0]
                b = perm[0][1]
                c = perm[1][0]
                d = perm[1][1]
                while (
                    (row := a + (a - c)) >= 0
                    and row < height
                    and (col := b + (b - d)) >= 0
                    and col < width
                ):
                    antinodes.add((row, col))
                    c = a
                    d = b
                    a = row
                    b = col
    return antinodes


if __name__ == "__main__":
    main()
