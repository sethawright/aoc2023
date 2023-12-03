from typing import Tuple

data: list[str] = open("aoc2023/inputs/day03.txt", "r").read().splitlines()


def inc_if_surrounding_symbol(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int], value: int
) -> Tuple[int, str]:
    (start_x, line) = start
    (end_x, _) = end

    # check if the surrounding box is valid
    # if it is, increment the value
    for y in range(line - 1, line + 2):
        if y < 0 or y > len(grid) - 1:
            continue

        for x in range(start_x - 1, end_x + 1):
            if x < 0 or x > len(grid[y]) - 1:
                continue
            try:
                print(y, x, grid[y][x])
                if grid[y][x] != "." and not grid[y][x].isdigit():
                    return (value, grid[y][x])
            except IndexError:
                print("index error")
                exit()

    return (0, "")


def main(lines: list[str]):
    sum = 0
    grid = []

    # split each line into a list of characters
    for line in lines:
        grid.append(list(line))

    # given the line, build a list numbers and the surrounding box
    for y, line in enumerate(grid):
        # build a cursor at the start of the line
        num = ""
        start_pos = None
        end_pos = None

        # move the cursor along the line
        for x, char in enumerate(line):
            # always move the cursor forward
            num = num or ""
            end_pos = (x, y)

            if char.isdigit():
                # if we detect a digit, begin "highlighting"
                # if the start position was already set
                # then we are already in highlighting mode
                start_pos = start_pos or (x, y)
                num += char
            elif start_pos is not None:
                # if it is not a digit, stop "highlighting"
                (inc, sym) = inc_if_surrounding_symbol(
                    grid, start_pos, end_pos, int(num)
                )
                sum += inc
                print(sum, sym, num, start_pos, end_pos)
                # print(sum, num, start_pos, end_pos)
                # reset the cursor's start position
                start_pos = None
                num = ""

        # line is finished, check if the last character was a digit
        if start_pos is not None and end_pos is not None:
            (inc, sym) = inc_if_surrounding_symbol(grid, start_pos, end_pos, int(num))
            sum += inc
            print(sum, sym, num, start_pos, end_pos)

    print(sum)


main(data)
