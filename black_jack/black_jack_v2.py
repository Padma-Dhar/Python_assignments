"""
Design doc:

class player
player can
1. draw a card
2. count his values
3. end game
4. show his cards

variables:
1. mapping between card and card value
2. cards drawn
3. sum of values of cards
4. did the player end game


computer:
computer can:
1. do everything the player can: (inheritance)
2. use_computer_logic to maximise wins

declare_winner_function 
1. sees the scores of both the player
"""


import random
from art import logo
from os import system, name

def stage1_loser(val1):
    if val1>21:
        return 1

def stage2_winner(val1,val2):
    if(val1>val2):
        return "Player"
    elif(val1 == val2):
        return "Draw"
    else:
        return "Computer"

def end_game_sequence(person, computer):
    if(person.win == 1):
        print("Player Won")
    elif(computer.win ==1):
        print("Computer Won")
    else:
        print("Draw")
    exit()
    

def move_cursor (y, x):
    print("\033[%d;%dH" % (y, x))

def print_logo():
    print(logo)

def affirmative(val):
    if(val.strip() == "y" or val.strip() == "yes" or str(val).strip() == "1" ):
        return 1
    return 0

def reload_screen(val):
    system("clear")
    print_logo()
    print("Your Cards: ")
    print(person.show_all_cards())
    print("Your sum: ", person.sum_of_cards)
    if(val==1):
        print("Computers Cards: ",computer.show_first_card())
    else:
        print("Computers Cards: ", computer.show_all_cards())
        print("Computers sum", computer.sum_of_cards)

class player:
    def __init__(self):
        self.cards_drawn_by_player=[]
        self.mapping = {
            "J":10,
            "Q":10,
            "K":10,
            "A":11
            }
        for card in range(1,11):
            self.mapping[card]=card
        self.sum_of_cards = 0
        self.is_game_ended = 0
        self.win = 0

    def draw_card(self):
        card=random.choice([2,3,4,5,6,7,8,9,10,"J","Q","K","A"])
        self.cards_drawn_by_player.append(card)
        self.count_value_of_cards()

    def show_all_cards(self):
        for cards in self.cards_drawn_by_player:
            print(cards, end=" ")
        print("")

    def count_value_of_cards(self):
        self.sum_of_cards=0
        for card in self.cards_drawn_by_player:
            self.sum_of_cards+=self.mapping[card]
        if(self.sum_of_cards>21):
            for location, card in enumerate(self.cards_drawn_by_player):
                if(card=="A"):
                    self.sum_of_cards-=10
                    self.cards_drawn_by_player[location]=1
    
    def end_game(self):
        self.is_game_ended=1


class computer_device(player):

    def computer_play_logic(self, exceed_val):
        reload_screen(2)
        self.exceed_val = exceed_val
        self.show_all_cards()
        if(self.sum_of_cards>self.exceed_val):
            self.end_game()
        while( 21 - self.sum_of_cards) >=11 and self.is_game_ended==0:
            self.draw_card()
            if(self.sum_of_cards>self.exceed_val):
                self.end_game()
            reload_screen(2)
            self.show_all_cards()
        while( 21 - self.sum_of_cards >=0 and self.is_game_ended==0):
           # print("choice with computer",self.sum_of_cards, (self.sum_of_cards-11)/10,(21-self.sum_of_cards)/10)
            if(self.sum_of_cards>self.exceed_val):
                self.end_game()
                break
            choice_taken=random.choices([0,1], weights=[(self.sum_of_cards - 11)/10,(21-self.sum_of_cards)/10], cum_weights=None, k=1)
            #print(choice_taken)
            #print(type(choice_taken))
            if(int(choice_taken[0])==1):
                self.draw_card()
                reload_screen(2)
               # self.show_all_cards()
            else:
                self.end_game()
                break

        self.end_game()

    def show_first_card(self):
        try:
            print(self.cards_drawn_by_player[0])
        except:
            print("No cards drawn as yet")




person = player()
computer = computer_device()
#reload_screen(1)

person.draw_card()
reload_screen(1)
person.draw_card()
reload_screen(1)

computer.draw_card()
reload_screen(1)
computer.draw_card()


while(person.is_game_ended!=1):
    draw_card = str(input("Draw another card ?"))
    if(affirmative(draw_card)):
        person.draw_card()
        reload_screen(1)
        if(stage1_loser(person.sum_of_cards) == 1):
            # 21 is exceeded, person lost
            person.win=-1
            computer.win=1
            end_game_sequence(person, computer)
    else:
        person.end_game()
        reload_screen(2)

computer.computer_play_logic(person.sum_of_cards)
reload_screen(2)
if(stage1_loser(computer.sum_of_cards)==1):
    person.win=1
    computer.win=-1
    end_game_sequence(person, computer)

if(stage2_winner(person.sum_of_cards, computer.sum_of_cards)=="Player"):
    person.win=1
    computer.win=-1
elif(stage2_winner(person.sum_of_cards,computer.sum_of_cards)=="Computer"):
    person.win=-1
    computer.win=1
end_game_sequence(person, computer)

