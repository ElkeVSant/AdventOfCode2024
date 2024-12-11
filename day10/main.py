#! /usr/bin/env python


def main():
    with open("day10/input.txt") as map:
        map = [[int(pos) for pos in line.rstrip()] for line in map]
    print(sum(score_trail_heads(map)))
    print(sum(rate_trail_heads(map)))


def score_trail_heads(map: list[list[int]]) -> list[int]:
    scores = []
    for loc in find_trailheads(map):
        scores.append(len(find_trail_ends(map, loc)))
    return scores


def rate_trail_heads(map: list[list[int]]) -> list[int]:
    ratings = []
    for loc in find_trailheads(map):
        ratings.append(rate_trail_head(map, loc))
    return ratings


def find_trailheads(map: list[list[int]]) -> list[tuple[int, int]]:
    return [
        (i, j)
        for i, line in enumerate(map)
        if 0 in line
        for j, val in enumerate(line)
        if val == 0
    ]


def find_trail_ends(
    map: list[list[int]],
    loc: tuple[int, int],
    trail_ends: set[tuple[int, int]] | None = None,
) -> set[tuple[int, int]]:
    height = map[loc[0]][loc[1]]
    if not trail_ends:
        trail_ends = set()
    if height == 9:
        trail_ends.add(loc)
    else:
        if loc[0] > 0 and map[loc[0] - 1][loc[1]] == height + 1:
            trail_ends = find_trail_ends(map, (loc[0] - 1, loc[1]), trail_ends)
        if loc[1] < len(map) - 1 and map[loc[0]][loc[1] + 1] == height + 1:
            trail_ends = find_trail_ends(map, (loc[0], loc[1] + 1), trail_ends)
        if loc[0] < len(map[0]) - 1 and map[loc[0] + 1][loc[1]] == height + 1:
            trail_ends = find_trail_ends(map, (loc[0] + 1, loc[1]), trail_ends)
        if loc[1] > 0 and map[loc[0]][loc[1] - 1] == height + 1:
            trail_ends = find_trail_ends(map, (loc[0], loc[1] - 1), trail_ends)
    return trail_ends


def rate_trail_head(map: list[list[int]], loc: tuple[int, int], rating: int = 0) -> int:
    height = map[loc[0]][loc[1]]
    if height == 9:
        rating += 1
    else:
        if loc[0] > 0 and map[loc[0] - 1][loc[1]] == height + 1:
            rating += rate_trail_head(map, (loc[0] - 1, loc[1]))
        if loc[1] < len(map) - 1 and map[loc[0]][loc[1] + 1] == height + 1:
            rating += rate_trail_head(map, (loc[0], loc[1] + 1))
        if loc[0] < len(map[0]) - 1 and map[loc[0] + 1][loc[1]] == height + 1:
            rating += rate_trail_head(map, (loc[0] + 1, loc[1]))
        if loc[1] > 0 and map[loc[0]][loc[1] - 1] == height + 1:
            rating += rate_trail_head(map, (loc[0], loc[1] - 1))
    return rating


if __name__ == "__main__":
    main()
