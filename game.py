from cards import Card
import random
class Game:

    def __init__(self):
        self.size = 4
        self.card_options = ['Red', 'Ken', 'Sum', 'Vic',
                             'Dog', 'Dan', 'Lap', 'Egg']
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')
        # print(self.locations)
        # for i in self.locations:
        #     print (i)
    def set_cards(self):
        '''
        this function returns a list if self.card_options instance attribute of
        the Game class with its members duplicated one time for pairing purposes
        for testing please un-comment the last two lines of the code and run the code
        '''
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations)-set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)
        #this line of code prints the number of cards
        #appended to the instance attribute >>> self.cards <<<
        # print(len(self.cards))

        # for i in self.cards:
        #     print(i)
        # print (self.cards)
        # for i in self.cards:
            # print (i)
    def create_row(self, num):
        row = []
        # self.columns = ['A', 'B', 'C', 'D']
        for column in self.columns:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    # print(card.location)
                    if card.matched:
                        row.append(str(card))
                        # print(str(card))
                        # print(row)
                    else:
                        row.append('    ')
                        # print(row)
                        # print (str (card))
        # testing to see every card's location
        # print (row)
        # print(card)
        return row

    def create_grid(self):
        #/ A / B / C / D /
        header = ' |   ' + '   |   '.join(self.columns) + '   |'
        print(header)
        for row in range(1, self.size + 1):
            print_row = f'{row}| '
            # print(print_row)
            get_row = self.create_row(row)
            print_row += '  | '.join(get_row) + '  |'
            print(print_row)

if __name__ == '__main__':
    Game()
    King = Game()
    King.set_cards()
    # King.create_row(2)
    for i in range(16):
        King.cards[i].matched = True
    # King.cards[0].matched = True
    # King.cards[1].matched = True
    # King.cards[2].matched = True
    # King.cards[3].matched = True
    # King.cards[4].matched = True
    # King.cards[5].matched = True
    # King.cards[6].matched = True
    # King.cards[7].matched = True
    # King.cards[8].matched = True
    King.create_grid()


    # for i in range(1, King.size + 1):
    #     print(i)
    # King.cards[0].matched = True
    # print(first_row)
    # print(King.create_row(1))
    # print(King.create_grid())

    # print(King.create_row(1))
    # print(King.create_row(4))
    # print(King.create_row(3))
    # print(King.create_row(2))
    # for card in King.cards:
    #     print (card)








