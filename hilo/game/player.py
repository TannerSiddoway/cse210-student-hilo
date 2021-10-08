
import random


class player:

    def __init__(self):
        pass
    def can_guess(self, score):
        return  (score > 0)
    
    def guess(self, deck):
        card = random.choice(deck)
        print(f'The card is : {card}')
        self.guess = input("Will the next card be higher or lower (hi/lo)")
        return card

    def correct_incorrect(self, card_1, deck):
        card_2 = card_1
        while card_1 == card_2:
            card_2 = random.choice(deck)
        if (card_1 > card_2) and self.guess.lower() == "lo":
            self.guess = "correct"
        if (card_1 > card_2) and self.guess.lower() == "hi":
            self. guess = 'incorrect'
        if (card_1 < card_2) and self.guess.lower() == "lo":
             self.guess = 'correct'
        if(card_1 > card_2) and self.guess.lower() == "hi":
            self.guess = 'incorrect'
        return self.guess
   
    def point_change(self, correct):
        if correct == 'correct':
            return 100
        if correct == 'incorrect':
            return -75