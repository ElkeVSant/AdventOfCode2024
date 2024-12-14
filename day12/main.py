#! /usr/bin/env python


def main():
    with open("day12/input.txt") as garden:
        plots = [line.rstrip() for line in garden]
    prices, bulk_prices = measure_regions(plots)
    print(sum(prices))
    print(sum(bulk_prices))


def measure_regions(plots: list[str]) -> tuple[list[int], list[int]]:
    prices = []
    bulk_prices = []
    checked = set()
    for i, line in enumerate(plots):
        for j, plot in enumerate(line):
            if (i, j) not in checked:
                area, perimeter, sides, region = map_region(plots, plot, (i, j))
                prices.append(area * perimeter)
                bulk_prices.append(area * sides)
                checked.update(region)
    return prices, bulk_prices


def map_region(
    plots: list[str],
    plants: str,
    pos: tuple[int, int],
    checked: set[tuple[int, int]] | None = None,
) -> tuple[int, int, int, set[tuple[int, int]]]:
    checked = checked if checked else set()
    area = 0
    perimeter = 0
    sides = 0
    if plots[pos[0]][pos[1]] != plants or pos in checked:
        return area, perimeter, sides, checked
    checked.add(pos)
    area += 1
    up = pos[0] > 0 and plots[pos[0] - 1][pos[1]] == plants
    down = pos[0] < len(plots) - 1 and plots[pos[0] + 1][pos[1]] == plants
    left = pos[1] > 0 and plots[pos[0]][pos[1] - 1] == plants
    right = pos[1] < len(plots[0]) - 1 and plots[pos[0]][pos[1] + 1] == plants
    if up:
        add_area, add_perimeter, add_sides, newly_checked = map_region(
            plots, plants, (pos[0] - 1, pos[1]), checked
        )
        area += add_area
        perimeter += add_perimeter
        sides += add_sides
        checked.update(newly_checked)
    else:
        perimeter += 1
    if down:
        add_area, add_perimeter, add_sides, newly_checked = map_region(
            plots, plants, (pos[0] + 1, pos[1]), checked
        )
        area += add_area
        perimeter += add_perimeter
        sides += add_sides
        checked.update(newly_checked)
    else:
        perimeter += 1
    if left:
        add_area, add_perimeter, add_sides, newly_checked = map_region(
            plots, plants, (pos[0], pos[1] - 1), checked
        )
        area += add_area
        perimeter += add_perimeter
        sides += add_sides
        checked.update(newly_checked)
    else:
        perimeter += 1
    if right:
        add_area, add_perimeter, add_sides, newly_checked = map_region(
            plots, plants, (pos[0], pos[1] + 1), checked
        )
        area += add_area
        perimeter += add_perimeter
        sides += add_sides
        checked.update(newly_checked)
    else:
        perimeter += 1
    if up + down + left + right == 0:
        sides += 4
    elif up + down + left + right == 1:
        sides += 2
    elif (not up or not down) and (not right or not left):
        sides += 1
    if up and right and plots[pos[0] - 1][pos[1] + 1] != plants:
        sides += 1
    if down and right and plots[pos[0] + 1][pos[1] + 1] != plants:
        sides += 1
    if down and left and plots[pos[0] + 1][pos[1] - 1] != plants:
        sides += 1
    if up and left and plots[pos[0] - 1][pos[1] - 1] != plants:
        sides += 1
    return area, perimeter, sides, checked


if __name__ == "__main__":
    main()
