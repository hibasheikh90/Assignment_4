
import math
import random

class Player:
    def __init__(self, letter):  # ✅ Fixed '__init__' method name
        # letter is 'X' or 'O'
        self.letter = letter

    def get_move(self, game):
        pass  # This will be implemented by child classes


class RandomComputerPlayer(Player):  # ✅ Fixed class name capitalization
    def __init__(self, letter):
        super().__init__(letter)  # ✅ Fixed '__init__' method name

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):  # ✅ Fixed class name capitalization
    def __init__(self, letter):
        super().__init__(letter)  # ✅ Fixed '__init__' method name    

    def get_move(self, game):  
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")

        return val  
