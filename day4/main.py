#! /usr/bin/env python

import re
from itertools import chain


def main():
    with open("day4/input.txt") as word_search:
        rows = [list(line.rstrip()) for line in word_search.readlines()]
    print(count_xmas(get_lines(rows)))
    print(count_x_mas(get_x_mas(rows)))


def count_x_mas(matches: list[tuple[int, int]]) -> int:
    return len(set([i for i in matches if matches.count(i) == 2]))


def get_x_mas(rows: list[list[str]]) -> list[tuple[int, int]]:
    [fdiags, bdiags] = get_diags(rows)
    flines = ["".join(fdiag) for fdiag in fdiags]
    blines = ["".join(bdiag) for bdiag in bdiags]
    matches = []
    size = int((len(blines) + 1) / 2) - 1
    for i in range(len(flines) - 1):
        for match in chain(
            re.finditer("MAS", flines[i]), re.finditer("SAM", flines[i])
        ):
            matches.append(
                (
                    match.start() + 1 + max(i - size, 0),
                    min(i, size) - (match.start() + 1),
                )
            )
        for match in chain(
            re.finditer("MAS", blines[i]), re.finditer("SAM", blines[i])
        ):
            matches.append(
                (
                    (max(0, (size) - i) + match.start() + 1),
                    max(0, i - size) + match.start() + 1,
                )
            )
    return matches


def count_xmas(lines: list[str]) -> int:
    return sum([line.count("XMAS") + line[::-1].count("XMAS") for line in lines])


def get_lines(rows: list[list[str]]) -> list[str]:
    [fdiags, bdiags] = get_diags(rows)
    lines = (
        ["".join(row) for row in rows]
        + ["".join(col) for col in list(map(list, zip(*rows)))]
        + ["".join(fdiag) for fdiag in fdiags]
        + ["".join(bdiag) for bdiag in bdiags]
    )
    return lines


def get_diags(rows: list[list[str]]) -> tuple[list[list[str]], list[list[str]]]:
    size = len(rows)
    fdiags = [[] for _ in range(size + size - 1)]
    bdiags = [[] for _ in range(len(fdiags))]
    for i in range(size):
        for j in range(size):
            fdiags[i + j].append(rows[i][j])
            bdiags[i - j - (-size + 1)].append(rows[j][i])
    return (fdiags, bdiags)


if __name__ == "__main__":
    main()
