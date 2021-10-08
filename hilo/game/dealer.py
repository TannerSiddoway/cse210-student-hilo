from game.player import player
import random
class dealer:
    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.player = player()
        self.card = 0
        self.correct = ""
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
            thrower(Thorwer): An instance of Thrower
        """
        self.card = self.player.guess()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.correct = self.player.correct_incorrect(self.card)
        points = self.player.point_change()
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"You were {self.correct}")
        print(f"Your score is: {self.score}")
        if self.player.can_guess():
            choice = input("guess again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False