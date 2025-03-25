import random

from card import Card, Rank, Suit

# Создали 52 разных карты
deck = []
for r in Rank.get_valid_values():
    for s in Suit.get_valid_values():
        c = Card(r, s)
        deck.append(c)

print(len(deck), deck)

# новая колода должна быть отсортированная
deck.sort()  # метод класса list, он уже нсть
print(deck)

# Хотим перемешать
random.shuffle(deck)
print(deck)

# Достать 5 карт
hand = set()  # пустое множество
for i in range(5):
    hand.add(deck.pop())

print(hand)
print(len(deck), deck)
