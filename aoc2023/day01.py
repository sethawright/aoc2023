import time
from typing import Tuple
import re

data: list[str] = open("aoc2023/inputs/day01.txt", "r").read().splitlines()

word_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# save time building map
# originally typecast but this is cleaner (maybe faster?)
for i in range(1, 10):
    word_map[str(i)] = i

# match digits and words
r_forward = r"(\d|one|two|three|four|five|six|seven|eight|nine)"

# used match last digit backwards then flip it
# did this to avoid splitting the string
r_backward = r"(\d|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)"


def find_first_last_digit(line: str) -> Tuple[int, int]:
    # reverse the line
    line_bw = line[::-1]

    match_forward = re.search(r_forward, line)
    match_backward = re.search(r_backward, line_bw)

    if not match_forward or not match_backward:
        raise ValueError("No match found for: " + line)

    # grab first matches
    first = match_forward.group(0)
    last = match_backward.group(0)
    last = last[::-1]

    if not first or not last:
        raise ValueError("Missing matching group" + line)

    # get the digit value
    start_digit = word_map.get(first)
    end_digit = word_map.get(last)

    if not start_digit or not end_digit:
        raise ValueError("Missing map value" + first + " " + last)

    print(line, start_digit, end_digit)
    return (start_digit, end_digit)


def main(data: list[str]):
    sum = 0
    for line in data:
        (start, end) = find_first_last_digit(line)
        sum = sum + (start * 10) + end

    print(sum)


start_time = time.time()
main(data)
print("--- %s ms ---" % ((time.time() - start_time) * 1000))
