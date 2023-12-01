LIMIT = 1000
data: list[str] = open("aoc2023/inputs/day01.txt", "r").read().splitlines()


def find_first_last_digit(line: str) -> (int, int):
    start_chars = line
    end_chars = start_chars[::-1]
    start_digit = extract_first_int(start_chars)
    end_digit = extract_first_int(end_chars)
    print(line, start_digit, end_digit)
    return (start_digit, end_digit)


def extract_first_int(chars: str) -> int:
    n = 0
    while n < LIMIT:
        start_n = get_int_from_str(chars[n])
        n += 1
        if start_n is not False:
            return start_n


def get_int_from_str(char: str) -> bool | int:
    try:
        n = int(char)
    except:
        return False

    return n


def main(data: list[str]):
    sum = 0
    for line in data:
        (start, end) = find_first_last_digit(line)
        sum = sum + (start * 10) + end

    print(sum)


main(data)
