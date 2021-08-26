"""
Design Document
1. Game object
2. FUnctions: 
    0. Generate a hidden number
    1. Set a level and the number of attempts accordingly # init function
    2. accept a number from the user while the number of attempts is not over. # sentence generator
    3. check if won or lost function

"""

import random

class Game:
    def __init__(self, level):
        self.number = self.get_random_number()
        self.level = level
        self.number_of_attempts = self.get_attempts()
        self.game_won =0
        self.check_if_won()

    def get_random_number(self):
        return random.randint(1,100)

    def get_attempts(self):
        if(self.level == "easy"):
            return 10
        elif( self.level == "medium"):
            return 7
        else:
            return 5
    
    def accept_number(self, number):
        self.number_of_attempts-=1
        if(number < self.number):
            print("Too Low")
        elif(number > self.number):
            print("Too High")
        else:
            print("Perfect")
            self.game_won = 1
        self.check_if_won()
    
    def check_if_won(self):
        if(self.game_won == 1):
            print("Game won")
            exit()
        elif( self.number_of_attempts ==0):
            print("Game Lost. Out of attempts")
            print("Number was ", self.number)
            exit()
        else:
            print("You have {} attempts left".format( self.number_of_attempts))


level_input = input("What level; easy, medium hard")
game_obj = Game(level_input)
while(1):
    input_value = input("Guess number")
    game_obj.accept_number(int(input_value))