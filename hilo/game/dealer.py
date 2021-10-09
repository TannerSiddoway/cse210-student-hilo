from game.player import player
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
            self (Dealer): an instance of Dealer.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Dealer): An instance of Dealer.
            player(player): An instance of player
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
        """Outputs the important game information for each round of play.

        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"You were {self.correct}")
        print(f"Your score is: {self.score}")
        if self.score > 0:
            choice = input("guess again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False