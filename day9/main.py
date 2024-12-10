#! /usr/bin/env python


def main():
    with open("day9/input.txt") as diskmap:
        diskmap = diskmap.readline().rstrip()
    print(sum([i * int(id) for i, id in enumerate(compact(convert(diskmap)))]))
    print(
        sum(
            [i * int(id) for i, id in enumerate(compact_unfragmented(convert(diskmap)))]
        )
    )


def convert(diskmap: str) -> list[list[str]]:
    unconverted = diskmap
    blocks = []
    id = 0
    while len(unconverted) >= 1:
        file_space = unconverted[0]
        blocks.append(int(file_space) * [str(id)])
        if len(unconverted) > 1:
            blocks.append(int(unconverted[1]) * ["."])
        unconverted = unconverted[2:]
        id += 1
    return blocks


def compact(blocks: list[list[str]]) -> list[str]:
    compacted = [blocks[0]]
    uncompacted = blocks[1:]
    while uncompacted:
        while "." in uncompacted[-1]:
            uncompacted.pop(-1)
        if "." not in uncompacted[0]:
            uncompacted.pop(0)
            compacted.append(uncompacted.pop(0))
        else:
            while "." in uncompacted[0]:
                if len(uncompacted[-1]) > 0:
                    uncompacted[0][uncompacted[0].index(".")] = uncompacted[-1][-1]
                    uncompacted[-1].pop(-1)
                else:
                    uncompacted.pop(-1)
                    uncompacted.pop(-1)
            compacted.append(uncompacted.pop(0))
            compacted.append(uncompacted.pop(0))
    return [id for file in compacted for id in file]


def compact_unfragmented(blocks: list[list[str]]) -> list[str]:
    compacted = blocks[:]
    j = 0
    for file in reversed(blocks):
        print(j)
        j += 1
        if file and "." not in file:
            needed_space = len(file)
            for i, free in enumerate(compacted):
                if "." in free:
                    free_space = len(free)
                    fi = compacted.index(file)
                    if needed_space <= free_space and i <= fi:
                        compacted[i] = ["."] * (free_space - needed_space)
                        compacted[fi] = ["."] * needed_space
                        compacted.insert(i, file)
                        break
    return [id if id != "." else "0" for file in compacted for id in file]


# TO DO: This runs way faster, but is as of yet incorrect (on input; correct on example)
# def compact_unfragmented(blocks: list[list[str]]) -> list[str]:
#     compacted = blocks[0][:]
#     uncompacted = blocks[1:]
#     while uncompacted:
#         while uncompacted and ("." in uncompacted[-1] or not uncompacted[-1]):
#             uncompacted.pop(-1)
#         if not uncompacted:
#             return compacted
#         space = len([s for s in uncompacted[0] if s == "."])
#         compacting = len(compacted)
#         for block in reversed(uncompacted):
#             if "." in block:
#                 continue
#             needed_space = len(block)
#             if needed_space <= space:
#                 for j in range(1, needed_space + 1):
#                     compacted.append(block[-j])
#                     block[-j] = "."
#                     uncompacted[0].pop(0)
#                 if not uncompacted[0]:
#                     uncompacted.pop(0)
#                     if "." not in uncompacted[0]:
#                         compacted.extend(uncompacted.pop(0))
#                 break
#         if compacting == len(compacted):
#             compacted.extend(["0"] * len(uncompacted.pop(0)))
#             if "." not in uncompacted[0]:
#                 compacted.extend(uncompacted.pop(0))
#     return compacted
#

if __name__ == "__main__":
    main()
