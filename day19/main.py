#! /usr/bin/env python

from functools import cache


def main():
    with open("day19/input.txt") as brand_guide:
        patterns, designs = brand_guide.read().rstrip().split("\n\n")
    patterns = tuple(patterns.split(", "))
    designs = designs.split("\n")
    compositions = []
    for design in designs:
        compositions.append(compose_design(design, patterns))
    # print(compositions)
    print(sum([1 for comp in compositions if comp]))
    print(sum(compositions))


@cache
def compose_design(
    design: str,
    patterns: tuple[str, ...],
) -> int:
    if not design:
        return 1
    compositions = 0
    for pattern in patterns:
        stripes = len(pattern)
        if design[:stripes] == pattern:
            compositions += compose_design(design[stripes:], patterns)
    return compositions


if __name__ == "__main__":
    main()
