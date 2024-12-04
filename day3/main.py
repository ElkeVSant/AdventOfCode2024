#! /usr/bin/env python

import re


def main():
    with open("day3/input.txt") as mem:
        mem = mem.read()
    print(execute((read_instructions(mem))))
    print(execute(read_cond_instructions(mem)))


def execute(instructions: list[str]) -> int:
    multiplications = [int(instr[0]) * int(instr[1]) for instr in instructions]
    return sum(multiplications)


def read_instructions(mem: str) -> list[str]:
    return re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", mem)


def read_cond_instructions(mem: str) -> list[str]:
    do = [0] + [m.end(0) for m in re.finditer("do\(\)", mem)]
    do_not = [m.end(0) for m in re.finditer("don't\(\)", mem)]
    instructions = []
    for i in do:
        mem_fragment = mem[
            i : min(int(j) for j in do + do_not + [len(mem) - 1] if j > i)
        ]
        instructions += read_instructions(mem_fragment)
    return instructions


if __name__ == "__main__":
    main()
