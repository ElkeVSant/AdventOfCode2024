#! /usr/bin/env python


def main():
    with open("day7/input.txt") as equations:
        equations = [
            (int(eq[0]), [int(n) for n in eq[1].rstrip().split(" ")])
            for line in equations
            if (eq := line.split(": "))
        ]
    print(
        sum(
            [
                eq[0]
                for eq in equations
                if evaluates(eq[0], eq[1][0], eq[1][1:], ["+", "*"])
            ]
        )
    )
    print(
        sum(
            [
                eq[0]
                for eq in equations
                if evaluates(eq[0], eq[1][0], eq[1][1:], ["+", "*", "||"])
            ]
        )
    )


def evaluates(
    test_value: int, result: int, eq: list[int], operators: list[str]
) -> bool:
    result = result
    rest_eq = eq[:]
    if result > test_value:
        return False
    nb = rest_eq.pop(0)
    if "+" in operators and (
        ((new_result := result + nb) == test_value and not rest_eq)
        or (rest_eq and evaluates(test_value, new_result, rest_eq, operators))
    ):
        return True
    if "*" in operators and (
        ((new_result := result * nb) == test_value and not rest_eq)
        or (rest_eq and evaluates(test_value, new_result, rest_eq, operators))
    ):
        return True
    if "||" in operators and (
        ((new_result := int(str(result) + str(nb))) == test_value and not rest_eq)
        or (rest_eq and evaluates(test_value, new_result, rest_eq, operators))
    ):
        return True
    return False


if __name__ == "__main__":
    main()
