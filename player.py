# Patric Natindim

# Player Class

class Player:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.score = 0
    
    def game_over(self):
        self.alive = False
        print(f"\nSorry, {self.name}. You lost the game.")
    
    def add_score(self, points):
        self.score += points
        print(f"{self.name}'s current score: {self.score}")
