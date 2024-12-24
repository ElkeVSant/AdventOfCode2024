#! /usr/bin/env python

import re
from enum import Enum
from dataclasses import dataclass


def main():
    with open("day17/input.txt") as debug_display:
        registers, program = debug_display.read().split("\n\n")
    _, a, b, c = re.split("\n{0,1}Register .: ", registers)
    registers = {"A": int(a), "B": int(b), "C": int(c)}
    program = [int(op) for op in program[9:].rstrip().split(",")]
    out = output(registers, program)
    print(",".join([str(val) for val in out]))
    registers["A"] = pow(8, len(program) - 1)
    print(calibrate(registers, program))


def calibrate(registers: dict[str, int], program: list[int]) -> int:
    length = len(program)
    for i in range(1, length + 1):
        while output(registers, program)[-i:] != program[-i:]:
            registers["A"] += pow(8, length - i)
    return registers["A"]


class Opcode(Enum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


class Operand(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7

    def literal(self) -> int:
        return self.value

    def combo(self, registers: dict[str, int]) -> int:
        if self.value == 4:
            return registers["A"]
        if self.value == 5:
            return registers["B"]
        if self.value == 6:
            return registers["C"]
        return self.value


@dataclass
class Instruction:
    opcode: Opcode
    operand: Operand
    pointer: int
    registers: dict[str, int]

    def execute(self) -> tuple[int | None, dict[str, int], int]:
        new_registers = self.registers.copy()
        new_pointer = self.pointer
        output = None
        match self.opcode:
            case Opcode.adv:
                new_registers["A"] = int(
                    self.registers["A"] / pow(2, self.operand.combo(self.registers))
                )
                new_pointer += 2
            case Opcode.bxl:
                new_registers["B"] = self.registers["B"] ^ self.operand.literal()
                new_pointer += 2
            case Opcode.bst:
                new_registers["B"] = self.operand.combo(self.registers) % 8
                new_pointer += 2
            case Opcode.jnz:
                if self.registers["A"] != 0:
                    new_pointer = self.operand.literal()
                else:
                    new_pointer += 2
            case Opcode.bxc:
                new_registers["B"] = self.registers["B"] ^ self.registers["C"]
                new_pointer += 2
            case Opcode.out:
                output = self.operand.combo(self.registers) % 8
                new_pointer += 2
            case Opcode.bdv:
                new_registers["B"] = int(
                    self.registers["A"] / pow(2, self.operand.combo(self.registers))
                )
                new_pointer += 2
            case Opcode.cdv:
                new_registers["C"] = int(
                    self.registers["A"] / pow(2, self.operand.combo(self.registers))
                )
                new_pointer += 2
        return output, new_registers, new_pointer


def output(registers: dict[str, int], program: list[int]) -> list[int]:
    pointer = 0
    outputs = []
    while pointer < len(program):
        opcode = Opcode(program[pointer])
        operand = Operand(program[pointer + 1])
        instruction = Instruction(opcode, operand, pointer, registers)
        output, registers, pointer = instruction.execute()
        if output is not None:
            outputs.append(output)
    return outputs


if __name__ == "__main__":
    main()
