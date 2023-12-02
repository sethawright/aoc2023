import re

data: list[str] = open("aoc2023/inputs/day02.txt", "r").read().splitlines()


def get_game_power(game: str):
    largest: dict[str, int] = dict(red=0, green=0, blue=0)
    pulls = re.findall(r"(\d+)\s(\w+)", game)

    for amount, color in pulls:
        largest[color] = max(largest[color], int(amount))

    return largest["red"] * largest["green"] * largest["blue"]


def main():
    power = 0

    for game in data:
        power += get_game_power(game)

    print(power)


main()
