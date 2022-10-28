# %%
import random
# %%
class RPS:
    def __init__(self, options_list):
        self.options_list = options_list
        self.computer_choice = random.choice(options_list)
        self.user_choice = input("Please choose one of rock, paper or scissors: ").lower()
        self.winner = str
    
    def get_computer_choice(self, computer_choice):
        return computer_choice
    
    def get_user_choice(self, user_choice):
        while user_choice not in self.options_list:
            user_choice = input("Sorry I didn't get this, please try again: ").lower()
        return user_choice
    
    def get_winner(self, computer_choice, user_choice, winner):
        computer = str
        user = str
        
        if computer_choice == user_choice:
            print ('Both players chose the same option. Try again!')
        elif (computer_choice == "Rock" and user_choice == "Scissors") or \
            (computer_choice == "Paper" and user_choice == "Rock") or \
            (computer_choice == "Scissors" and user_choice == "Paper"):
            winner = computer
            print(f'The computer chose {computer_choice}. The computer wins')
        else:
            winner = user
            print(f'The computer chose {computer_choice}. The user wins')

        return winner
# %%
def play():
    options_list = ["rock", "paper", "scissors"]
    game = RPS(options_list)
    game.get_computer_choice(game.computer_choice)
    game.get_user_choice(game.user_choice)
    game.get_winner(game.computer_choice, game.user_choice, game.winner)
# %%
play()
# %%
