
import random


class player:

    def __init__(self):
        self.guess = ""
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    def can_guess():
        return  (self.score > 0)
    
    def guess(self):
        card = random.choice(self.deck)
        print(f'The card is : {card}')
        self.guess = input("Will the next card be higher or lower (hi/lo)")
        return card

    def correct_incorrect(self, card_1):
        card_2 = card_1
        while card_1 == card_2:
            card_2 = random.choice(self.deck)
        if (card_1 > card_2) and self.guess.lower() == "lo":
            self.guess = 'correct'
        elif (card_1 > card_2) and self.guess.lower() == "hi":
            self. guess = 'incorrect'
        elif (card_1 < card_2) and self.guess.lower() == "lo":
             self.guess = 'correct'
        elif(card_1 > card_2) and self.guess.lower() == "hi":
            self.guess = 'incorrect'
        return self.guess
   
    def point_change(self):
        if self.guess == 'correct':
            return 100
        elif self.guess == 'incorrect':
            return -75