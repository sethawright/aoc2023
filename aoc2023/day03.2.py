data: list[str] = open("aoc2023/inputs/day03.txt", "r").read().splitlines()


def check_bounding_box(grid: list[list[str]], position: tuple[int, int]) -> int:
    (line, x) = position
    nums = []

    # check the 8 surrounding boxes
    for y in range(line - 1, line + 2):
        if y < 0 or y > len(grid) - 1:
            continue

        for i in range(x - 1, x + 2):
            print(y, i, grid[y][i])
            if i < 0 or x > len(grid[y]) - 1:
                continue
            try:
                if grid[y][i].isdigit():
                    print("found digit")
                    # this could probably be more efficient but I'm lazy
                    sur = find_surrounding_number(grid, (y, i))
                    print(sur)
                    nums.append(sur)
            except IndexError:
                print("index error ln %s %s" % (y + 1, i + 1))
                exit()

    # filter out duplicated numbers
    nums = list(set(nums))
    if len(nums) == 2:
        print("found 2")
        print(line, x, nums, nums[0] * nums[1])
        return nums[0] * nums[1]
    elif len(nums) > 2:
        raise Exception("Too many numbers in bounds")
    else:
        print("not enough numbers surrounding")
        return 0


def find_surrounding_number(grid: list[list[str]], position: tuple[int, int]) -> int:
    # walk x position backwards and forwards until finding a non-digit
    (y, x) = position
    num: str = grid[y][x]
    print("check box num")

    dx = x
    while True:
        dx -= 1
        if dx >= 0 and grid[y][dx].isdigit():
            num = grid[y][dx] + num
            print(num)
        else:
            break

    dx = x
    while True:
        dx += 1
        if dx <= len(grid[y]) - 1 and grid[y][dx].isdigit():
            num = num + grid[y][dx]
            print(num)
        else:
            break

    return int(num)


def main(lines: list[str]):
    sum = 0
    grid = []

    # split each line into a list of characters
    for line in lines:
        grid.append(list(line))

    # find a * gear character
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "*":
                sum += check_bounding_box(grid, (y, x))

    print(sum)


main(data)
