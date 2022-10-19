# %%
import cv2
from keras.models import load_model
import numpy as np
import random
import time

# %%
class RPS:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape = (1, 224, 224, 3), dtype = np.float32)
        self.computer_wins = 0
        self.user_wins = 0
    

    def get_countdown(self):
        self.countdown = 3
        print("Show your choice in...")
        while self.countdown > 0:
            print(f'{self.countdown}')
            cv2.waitKey(500)
            self.countdown -= 1
        print("Show your choice now!!!")

    


    def get_computer_choice(self):
        self.options = {}
        with open('labels.txt') as file:
            for info in file:
                k, v = info.split()
                self.options[k] = v
        self.computer_choice = random.choice(list(self.options.values())).lower()
        return self.computer_choice
    
    
    def get_camera(self):
        self.end_time = time.time() + 1
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
        print(self.prediction) 
        return self.prediction
        
    def get_user_choice(self):
        self.prediction = self.get_prediction()
        self.user_choice = np.argmax(self.prediction[0])
        return self.user_choice   
    
    
    def get_winner(self, computer_choice, user_choice): 
        if computer_choice == user_choice:
            print(f'Tie! Both players chose {computer_choice}')
        elif (computer_choice == "Rock" and user_choice == "Scissors") or \
            (computer_choice == "Paper" and user_choice == "Rock") or \
            (user_choice == "Paper" and computer_choice == "Rock") :
            self.computer_wins += 1
            print(f'The computer chose {computer_choice}. The computer wins the round')
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

    game.cap.release() # After the loop release the cap object
    cv2.destroyAllWindows()    
# %%
play_game()
# %%