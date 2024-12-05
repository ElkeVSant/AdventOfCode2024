#! /usr/bin/env python

import math


def main():
    with open("day5/input.txt") as input:
        rules, updates = input.read().rstrip().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]
    correct_updates, corrected_updates = divide_updates(updates, rules)
    print(sum(get_middles(correct_updates)))
    print(sum(get_middles(corrected_updates)))


def divide_updates(
    updates: list[list[int]], rules: list[list[int]]
) -> tuple[list, list]:
    correct_updates = []
    corrected_updates = []
    for update in updates:
        verification, rule = verify(update, rules)
        if verification:
            correct_updates.append(update)
        else:
            while not verification:
                assert rule
                update = correct(update, rule)
                verification, rule = verify(update, rules)
            corrected_updates.append(update)
    return correct_updates, corrected_updates


def verify(update: list[int], rules: list[list[int]]) -> tuple[bool, list[int] | None]:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False, rule
    return True, None


def correct(update: list[int], rule: list[int]) -> list[int]:
    first = update.index(rule[1])
    second = update.index(rule[0])
    return (
        update[:first]
        + update[first + 1 : second + 1]
        + [rule[1]]
        + update[second + 1 :]
    )


def get_middles(updates: list[list[int]]) -> list[int]:
    return [update[math.floor(len(update) / 2)] for update in updates]


if __name__ == "__main__":
    main()
