
import random


class player:

    def __init__(self):
        self.choice = ""
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
    def guess(self):
        card = int(random.choice(self.deck))
        print(f'The card is : {card}')
        self.choice = input("Will the next card be higher or lower (hi/lo) ")
        return card

    def correct_incorrect(self, card_1):
        card_2 = card_1
        while card_1 == card_2:
            card_2 = random.choice(self.deck)
        print(f'The second card is {card_2}')
        if (card_1 > card_2) and self.choice.lower() == "lo":
            self.choice = 'correct'
        elif (card_1 > card_2) and self.choice.lower() == "hi":
            self.choice = 'incorrect'
        elif (card_1 < card_2) and self.choice.lower() == "lo":
             self.choice = 'correct'
        elif(card_1 > card_2) and self.choice.lower() == "hi":
            self.choice = 'incorrect'
        return self.choice
   
    def point_change(self):
        if self.choice == 'correct':
            return 100
        elif self.choice == 'incorrect':
            return -75
