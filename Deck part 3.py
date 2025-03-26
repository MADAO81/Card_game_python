import random
from card import Card, Rank, Suit

class Deck:
    def __init__(self):
        self.cards = []
        for r in Rank.get_valid_values():
            for s in Suit.get_valid_values():
                c = Card(r, s)
                self.cards.append(c)
        self.cards.sort()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n):
        hand = set()  # пустое множество
        for i in range(5):
            hand.add(self.cards.pop())
        return hand

    def __repr__(self):
        return repr(self.cards)


d = Deck()

print(d)

# Перемешали
d.shuffle()
print(d)

# Достали 5 карт
hand = d.draw(5)
print(d)
print(hand)

# for card in d:
#     print(card)

#d.cards[2] = 'hello'
#print(d)

#c = Card(5, 'hearts')
#print(c in d)

print(len(d))