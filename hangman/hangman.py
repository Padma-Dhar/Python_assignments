from os import system, name
from time import sleep
import random
import word_list as word_list
class hangman:
    def generate(self):
        return random.choice(word_list.list_of_objects)

    def __init__(self):
        self.word=self.generate()
        self.guess=0
        self.guessed_letter=set()
        self.display_word=""
        self.display_word+="_"*len(self.word)
        print(self.display_word)

    def print_logo(self):
        str="""                                     _____
                |    |  /\\   |\\  |   |        |\\  /|    /\\   |\\  |
                |----| /--\\  | \\ |   |  ___   | \\/ |   /--\\  | \\ |  
                |    |/    \\ |  \\|   |___|    | \\/ |  /    \\ |  \\|"""
        print(str)

    def reload_screen(self):
        system("clear")
        self.move_cursor(10,10)
        self.display()
        self.move_cursor(20,20)
        self.display_man(80)
        self.move_cursor(100,10 )
        self.print_logo()
        self.move_cursor(0,0)

    def custom_message(self, msg):
        self.reload_screen()
        self.move_cursor(100,80)
        print(msg)

    def check_if_won(self):
        if(self.guess < 6 and "_" not in self.display_word ):
            self.custom_message("You won")
            exit()
        
    def check_if_lost(self):
        if(self.guess>=6):
            self.custom_message("You lost")
            exit()

    def guess_letter(self, letter):
        self.reload_screen()
        if(letter not in self.guessed_letter and letter in self.word):
            self.add_letter(letter)
            self.check_if_won()
        elif (letter in self.guessed_letter):
            self.custom_message("You already guessed this")
        else:
            self.guess+=1
            self.check_if_lost()
        self.reload_screen()

    # display the current amount of guessed word and print it out
    def display(self, letter=""):
        print(self.display_word)

    def add_letter(self,letter):
        if(letter in self.word and letter not in self.guessed_letter):
            for index,value in enumerate(self.word):
                if(value==letter):
                    self.display_word=self.display_word[:index]+letter+self.display_word[index+1:]
        self.guessed_letter.add(letter)

    def move_cursor (self, y, x):
        print("\033[%d;%dH" % (y, x))

    # will display the man at the current number of guesses
    def display_man(self,indent):

        print(" "*50+"-------")
        print(" "*50+"  |")
        print(" "*50+"  |")
        if(self.guess >= 1):
            #display the head

            print(" "*50+"  O")
        if(self.guess == 2):
            print(" "*50+"  |")
        if(self.guess == 3):
            print(" "*50+" /|")
        if(self.guess >= 4):
            print(" "*50+" /|\\ ")
        if(self.guess ==5):
            print(" "*50+" /")
        if(self.guess == 6):
            print(" "*50+" /\\ ")

hangman_object = hangman()
while(1):
    entered_letter=str(input("guess letter"))
    hangman_object.guess_letter(entered_letter)
