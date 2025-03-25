import random

class Weightable:  # Абстрактный класс, он служит только в качестве родителя
    def __gt__(self, other):
        return self.weights[self.value] > self.weights[other.value]

    def __lt__(self, other):
        return self.weights[self.value] < self.weights[other.value]

    def __ge__(self, other):
        return self.weights[self.value] >= self.weights[other.value]

    def __le__(self, other):
        return self.weights[self.value] <= self.weights[other.value]

    def __eq__(self, other):
        return self.weights[self.value] == self.weights[other.value]

    def __ne__(self, other):
        return self.weights[self.value] != self.weights[other.value]


class Suit(Weightable):
    valid_values = {'hearts', 'spades', 'clubs', 'diamonds'}

    weights = {  # ♠<♦<♣<♥
        'hearts': 1,
        'clubs': 2,
        'diamonds': 3,
        'spades': 4,
    }

    symbols = {
        'hearts': '\u2665',
        'clubs': '\u2663',
        'diamonds': '\u2666',
        'spades': '\u2660',
    }

    def __init__(self, value):
        if value not in self.valid_values:
            raise ValueError('Неправильное название масти')

        self.value = value

    def __repr__(self):
        return self.symbols[self.value]

    @classmethod  # тут мы обращаемся к атрибуту класса, а не самого объекта
    def get_valid_values(cls):  # на место cls попадёт не экземпляр, а тип, в данном случае Suit
        return list(cls.valid_values)

class Rank(Weightable):
    valid_values = {2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'}  # общее для всех экземпляров

    weights = {
        2: 101,
        3: 102,
        4: 103,
        5: 104,
        6: 105,
        7: 106,
        8: 107,
        9: 108,
        10: 109,
        'J': 110,
        'Q': 111,
        'K': 112,
        'A': 113
    }

    def __init__(self, value):
        if value not in self.valid_values:
            raise ValueError('Неправильное старшинство')

        self.value = value

    def __repr__(self):
        return str(self.value)

    @classmethod
    def get_valid_values(cls):  # на место cls попадёт не экземпляр, а тип, в данном случае Suit
        return list(cls.valid_values)

class Card:
    def __init__(self, rank, suit):
        self.rank = Rank(rank)
        self.suit = Suit(suit)

    def __repr__(self):
        return repr(self.rank) + repr(self.suit)

    def __gt__(self, other):  # >
        if self.suit != other.suit:
            return self.suit > other.suit
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    @staticmethod  # когда не нужен self
    def random():  # это называется фабрика (factory)
        r = random.choice(Rank.get_valid_values())
        s = random.choice(Suit.get_valid_values())
        return Card(r, s)

    def __hash__(self):
        # return hash(repr(self))
        # return Rank.weights[self.rank.value] * 1000 + Suit.weights[self.suit.value]
        return hash((Rank.weights[self.rank.value], Suit.weights[self.suit.value]))
        #return hash((hash(self.rank), hash(self.suit)))