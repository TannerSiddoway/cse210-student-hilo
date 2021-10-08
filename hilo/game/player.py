
class player(score):

    def __init__(self):
        self.score = score

    def can_guess():
        return  (self.score > 0)
    
    def guess(card_1, card_2):
        guess = input("Higher/Lower")
        if (card_1 > card_2) and guess.lower() == "lower":
            guess = 'correct'
        elif (card_1 > card_2) and guess.lower() == "higher":
            guess = 'incorrect'
        elif (card_1 < card_2) and guess.lower() == "lower":
            guess = 'correct'
        elif(card_1 > card_2) and guess.lower() == "higher":
            guess = 'incorrect'
        return guess
    def point_change(guess, score):
        if guess == 'correct':
            score += 100
        else:
            score -= 75
        return score    
