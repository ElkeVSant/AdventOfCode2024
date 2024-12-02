#! /usr/bin/env python

import copy


def main():
    with open("day2/input.txt") as reports:
        levels = [[int(level) for level in report.split()] for report in reports]
    print(count_safe(levels))
    dampened_levels = dampen_levels(levels)
    print(count_safe(dampened_levels))


def count_safe(levels: list[list[int]]) -> int:
    difs = differ(levels)
    safe_count = 0
    for level_difs in difs:
        if len([dif for dif in level_difs if 0 < abs(dif) < 4]) == len(
            level_difs
        ) and len([dif for dif in level_difs if dif > 0]) in (0, len(level_difs)):
            safe_count += 1
    return safe_count


def dampen_levels(levels: list[list[int]]) -> list[list[int]]:
    dampened_levels = copy.deepcopy(levels)
    difs = differ(levels)
    for level_ind, level_difs in enumerate(difs):
        if len([dif for dif in level_difs if 0 < abs(dif) < 4]) in (
            len(level_difs) - 1,
            len(level_difs) - 2,
        ):
            index = [
                i
                for i, level_dif in enumerate(level_difs)
                if 1 > abs(level_dif) or abs(level_dif) > 3
            ]
            dampened_levels[level_ind] = dampen_level(
                dampened_levels[level_ind], index[0]
            )
        elif 0 < len([dif for dif in level_difs if dif > 0]) < 3:
            index = [i for i, level_dif in enumerate(level_difs) if level_dif > 0]
            dampened_levels[level_ind] = dampen_level(
                dampened_levels[level_ind], index[0]
            )
        elif 0 < len([dif for dif in level_difs if dif < 0]) < 3:
            index = [i for i, level_dif in enumerate(level_difs) if level_dif < 0]
            dampened_levels[level_ind] = dampen_level(
                dampened_levels[level_ind], index[0]
            )
    #    print(dampened_levels)
    return dampened_levels


def dampen_level(level: list[int], index: int) -> list[int]:
    if count_safe([level[:index] + level[index + 1 :]]) == 1:
        return level[:index] + level[index + 1 :]
    return level[: index + 1] + level[index + 2 :]


def differ(levels: list[list[int]]) -> list[list[int]]:
    return [
        [level1 - level2 for level1, level2 in zip(level, level[1:])]
        for level in levels
    ]


if __name__ == "__main__":
    main()
