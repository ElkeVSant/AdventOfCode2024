#! /usr/bin/env python


def main():
    with open("day19/input.txt") as brand_guide:
        patterns, designs = brand_guide.read().rstrip().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    print(sum([compose_design(design, patterns) for design in designs]))


def compose_design(design: str, patterns: list[str]) -> bool:
    for pattern in patterns:
        stripes = len(pattern)
        if design[:stripes] == pattern:
            if stripes == len(design) or compose_design(design[stripes:], patterns):
                return True
    return False


if __name__ == "__main__":
    main()
