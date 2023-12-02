import re

data: list[str] = open("aoc2023/inputs/day02.txt", "r").read().splitlines()
limits: dict[str, int] = dict(red=12, green=13, blue=14)


def validate_game(game: str):
    search = re.search(r"Game (\d+)\:", game)
    id = search is not None and search.group(1)
    pulls = re.findall(r"(\d+)\s(\w+)", game)

    for amount, color in pulls:
        if int(amount) > limits[color]:
            return 0

    return int(id)


def main():
    valid_games = 0

    for game in data:
        valid_games += validate_game(game)

    print(valid_games)


main()
