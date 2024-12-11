#! /usr/bin/env python

from functools import cache


def main():
    with open("day11/input.txt") as stones:
        stones = [int(stone) for stone in stones.read().rstrip().split(" ")]

    print(sum([blink(stone, 25) for stone in stones]))
    print(sum([blink(stone, 75) for stone in stones]))


@cache
def blink(stone: int, amount: int) -> int:
    if amount == 0:
        return 1
    new_stones = []
    if stone == 0:
        return blink(1, amount - 1)
    else:
        digits = len(str(stone))
        if digits % 2 == 0:
            div = int(pow(10, (digits / 2)))
            left = int(stone / div)
            right = stone - left * div
            return blink(left, amount - 1) + blink(right, amount - 1)
        else:
            return blink(stone * 2024, amount - 1)


if __name__ == "__main__":
    main()
