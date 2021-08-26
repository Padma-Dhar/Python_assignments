# from art import logo
# import random

# class blackjack_player:

#     def __init__(self):
#         self.blackjack_cards_drawn = []
#         self.end_game_parameter=0
#         self.lost=0
#         self.sum_of_card_value=0
#         self.card_value={"J":10,"Q":10,"K":10,"A":11}
#         for i in range(1,11):
#             self.card_value[i]=int(i)

#     def draw_card(self):
#         card=random.choice([2,3,4,5,6,7,8,9,10,"J","Q","K","A"])
#         self.blackjack_cards_drawn.append(card)
#         self.check_if_lost()

#     def end_game(self):# return 1 if the player has end the game
#         self.end_game_parameter = 1

#     def reveal_card(self):
#         for i in self.blackjack_cards_drawn:
#             if(i==1):
#                 print(" A ", end="")
#             else:
#                 print(" "+str(i)+' ',end="")
#         print()

#     def count_score(self):
#         self.sum_of_card_value=0
#         for card in self.blackjack_cards_drawn:
#             self.sum_of_card_value+=self.card_value[card]

#         if(self.sum_of_card_value>21):
#             for location, card in enumerate(self.blackjack_cards_drawn):
#                 print(self.card_value)
#                 print(self.blackjack_cards_drawn)
#                 try:
#                     print(self.card_value[card])
#                 except:
#                     print("probelme")
#                 print(card,location)
#                 if(self.card_value[card] == 11):
#                     self.blackjack_cards_drawn[location]=1
#                     self.sum_of_card_value-=10
#                     break


#     def check_if_lost(self):# goes over 21
#         self.count_score()
#         if(self.sum_of_card_value>21):
#             self.lost=1


# player = blackjack_player()
# computer = blackjack_player()

# while(input("Play a game of blackjack")=="y"):
#     player.draw_card()
#     player.draw_card()
#     player.reveal_card()
#     computer.draw_card()
#     computer.reveal_card()
#     computer.draw_card()
#     while(input("Draw a card") == "y"):
#         player.draw_card()
#         player.reveal_card()
#         if(player.lost==1):
#             break
#     player.end_game()
#     computer.reveal_card()

#     while(computer.sum_of_card_value<player.sum_of_card_value and computer.lost==0 and computer.end_game_parameter != 1 and player.lost==0):
#         computer.count_score()
#         score_left=21-computer.sum_of_card_value
#         if(score_left>10):
#             computer.draw_card()
#             computer.reveal_card()
#         elif(score_left<=10):
#             choice_by_computer = random.choices([0,1], weights=[(10-score_left)/10, score_left/10], cum_weights=None, k=1)
#             if(choice_by_computer == 1):
#                 #pick a card
#                 computer.draw_card()
#                 computer.reveal_card()
#             else:
#                 computer.end_game()

#     print("Your cards", player.reveal_card())
#     print("Computers Cards", computer.reveal_card())

#     if(computer.lost==1 or (computer.sum_of_card_value<player.sum_of_card_value and player.lost==0)):
#         print("You Win")
#     elif((computer.lost==0 and computer.sum_of_card_value>player.sum_of_card_value) or player.lost == 1):
#         print("You lose")
#     else:
#         print("Draw")