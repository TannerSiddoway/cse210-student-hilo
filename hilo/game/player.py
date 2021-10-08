
class player:

    def __init__(self):
        self.guess = ""

    def can_guess():
        return  (self.score > 0)
    
    def guess(self, card_1, card_2):
        self.guess = input("Will the next card be higher or lower (hi/lo)")
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