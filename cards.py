class Card:
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False

    def __eq__(self, other):
        return self.card == other.card

    def __str__(self):
        return str(self.card)

if __name__ == '__main__':
    print('this python file works like a charm, do not worry about it')
else:
    print('thanks for importing cards module')
    # card1 = Card('egg', 'A!')
    # card2 = Card('egg', 'B1')
    # card3 = Card('Egg', 'D4')
    #
    # print(card1 == card2)
    # print(card1 == card3)
    # print(card1)
    # print(card1.matched())
