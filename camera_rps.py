# %%
import cv2
from keras.models import load_model
import numpy as np
import random
import time
# %%
class RPS:

    '''
    A game of "Rock, Paper, Scissors", where the user plays
    against the computer. The user shows their choice through
    the camera, while the computer's choice is determined
    randomly.

    Attributes:
    ----------
    model: load_model('keras_model.h5')
        Loads the computer vision model that will be used to
        play the game.
    
    cap: cv2VideoCapture(0)
        Allows video to be captured
    
    data: Numpy array
        The number of images you can put into the array is
        determined by the first position in the shape tuple,
        in this case 1.

    computer_wins: int
        The number of wins the computer has at the start of the game.

    user_wins: int
        The number of wins the user has at the start of the game

    
    Methods:
    -------
    get_countdown(): 
        Provides a countdown before the user is asked to show their choice.
    
    get_computer_choice():
        Randomly selects the computer's choise from a given list.
    
    get_camera():
        Activates the camera

    get_prediction():
        Understands the user's input with the use of probabilities
    
    get_user_choice():
        Uses the list of probabilities provided by get_prediction()
        to determine which gesture the inputted image corresponds to.

    get_winner():
        Determines the winner of each game.
    '''
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape = (1, 224, 224, 3), dtype = np.float32)
        self.computer_wins = 0
        self.user_wins = 0

    def get_countdown(self):
        print("Show your choice in...")
        self.countdown = 3
        while self.countdown > 0:
            self.minute, sec = divmod(self.countdown, 60)
            timer = f"{sec}"
            cv2.waitKey(1000)
            print(f"{timer}")
            self.countdown -= 1
    
    def get_computer_choice(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.computer_choice = random.choice(self.options)
        return self.computer_choice
    
    def get_camera(self):
        self.end_time = time.time() + 3
        while self.end_time > time.time():
            self.ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            self.normalized_image = (image_np.astype(np.float32) / 127.0) - 1
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return self.normalized_image
    
    def get_prediction(self):
        self.data[0] = self.get_camera()
        self.prediction = self.model.predict(self.data) 
        return self.prediction
        
    def get_user_choice(self):
        self.prediction = self.get_prediction()
        self.options_list = ["Rock", "Paper", "Scissors", "Nothing"]
        self.user_choice = self.options_list[np.argmax(self.prediction[0])]
        return self.user_choice   
    
    def get_winner(self, computer_choice, user_choice): 
        if computer_choice == user_choice:
            print(f'Tie! Both players chose {computer_choice}')
        elif (computer_choice == "Rock" and user_choice == "Scissors") or \
            (computer_choice == "Paper" and user_choice == "Rock") or \
            (computer_choice == "Scissors" and user_choice == "Paper"):
            self.computer_wins += 1
            print(f'The computer chose {computer_choice}. The computer wins the round')
        elif user_choice == "Nothing":
            print("Sorry, I didn't get that, try again!")
        else:
            self.user_wins += 1
            print(f'The computer chose {computer_choice}. The user wins the round')
# %%
def play_game():
    game = RPS()
    while game.computer_wins < 3 or game.user_wins < 3:
        
        game.get_countdown()
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        
        print(f'The computer has won {game.computer_wins} times')
        print(f'You have won {game.user_wins} times')
        
        if game.user_wins == 3:
            print('You win the game!')
            break
        elif game.computer_wins == 3:
            print('The computer wins the game!')
            break

    # After the loop release the cap object
    game.cap.release() 
    # Destrol all windows
    cv2.destroyAllWindows()    
# %%
play_game()
# %%