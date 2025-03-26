import random
from card import Card, Rank, Suit

class Deck(list):
    def __init__(self):
        for r in Rank.get_valid_values():
            for s in Suit.get_valid_values():
                c = Card(r, s)
                self.append(c)

        self.sort()  # метод класса list, он уже есть

    def shuffle(self):
        random.shuffle(self)  # потом можно заменить на более непредсказуемый RNG, например, из модуля secrets

    def draw(self, n):
        hand = set()  # пустое множество
        while len(hand) <= n:
            hand.add(self.pop())
        return hand

# Создали колоду, уже отсортированная, 52 карты
d = Deck()

print(len(d), d)

# Перемешали
d.shuffle()
print(len(d), d)

# Достали 5 карт
hand = d.draw(5)
print(len(d), d)
print(hand)

# что нам досталось бонусом, это плохо и хорошо
# for card in d:
#     print(card)

print(d[-5])
d.append('hello')
d[2] = 'hi'
print(len(d), d)