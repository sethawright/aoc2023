import re
import functools as ft
from dataclasses import dataclass, field

data: list[str] = open("aoc2023/inputs/day04.txt", "r").read().splitlines()


@dataclass
class ScratchCard:
    input: str
    card_numbers: list[int] = field(default_factory=list)
    winning_numbers: list[int] = field(default_factory=list)
    copies = 1
    wins = 0
    value = 0
    matches: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.input = self.input.split(":")[1]
        sets = self.input.split("|")
        self.winning_numbers = re.findall(r"(\d+)", sets[0])
        self.card_numbers = re.findall(r"(\d+)", sets[1])
        self.matches = self.get_matches()
        self.wins = len(self.get_matches())
        self.value = self.get_card_value()

    def get_matches(self) -> list[int]:
        return list(set(self.winning_numbers) & set(self.card_numbers))

    def get_card_value(self) -> int:
        val = 0
        if self.wins > 1:
            val = 2 ** (self.wins - 1)
        elif self.wins == 1:
            val = 1
        return val


def main(input: list[str]):
    # part 1
    cards: list[ScratchCard] = [ScratchCard(ln) for ln in input]
    points: int = ft.reduce(lambda a, b: a + b, [card.value for card in cards])
    print(points)

    # part 2
    for i, card in enumerate(cards):
        if card.wins > 0:
            print("Card %s:" % (i + 1), card.wins)

            for n in range(i + 1, i + card.wins + 1):
                cards[n].copies += card.copies

    copies = ft.reduce(lambda a, b: a + b, [card.copies for card in cards])
    print(copies)


main(data)
