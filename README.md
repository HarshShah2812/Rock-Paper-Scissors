# Rock-Paper-Scissors

## Overview

"Rock, Paper, Scissors" is a game whereby 2 players simultaneously show one of three gestures - rock, paper or scissors. Rock beats scissors, paper beats rock, and scissors beats paper. If your hand gesture beats that of the other player, you win the game; if both players show the same hand signal, it's a draw. In this project, the user will play the game against the computer via camera.

## Learning objectives

- Creating machine learning models;
- setting up virtual environments and installing the required packages;
- practising intermediate level Python i.e. Object Oriented Programming, If/Else statements, 'While' loops.

## Tools

- VS Code
- Git
- Github

## The model

Using "Teachable Machine" to create a dataset with 4 different classes: "Rock, Paper, Scissors, Nothing", the files corresponding to the dataset are then downloaded: "keras_model.h5" and "labels.txt"; the former contains the structure of the model and the latter contains the parameters. They will later be loaded to use in a Python script that will simulate a "Rock, Paper, Scissors" game.

Below, you can see pictures taken that represent each of the different classes:

Rock

![Rock 1](https://user-images.githubusercontent.com/67421468/198841057-79e60def-b4e9-4787-bd8d-cc33d51601be.png)

Paper

![Paper 1](https://user-images.githubusercontent.com/67421468/198841109-60ce89eb-75a6-4ee7-b1e8-1dd922e5f051.png)

Scissors

![Scissors 1](https://user-images.githubusercontent.com/67421468/198841123-62cac48f-5281-4fd2-a79d-ed4c11eb65cd.png)

Nothing

![Nothing](https://user-images.githubusercontent.com/67421468/198841141-baf63f3f-85ca-4c21-8438-a8893f2284aa.png)


### Creating the dataset

In order to try and ensure that the model is as accurate as possible, 2 main factors have been taken into consideration, which where the hands themselves (left/right), as well as the setting (capturing images in 3 different room). 

Below, there are images to demonstrate these 2 factors:

Left vs Right:

![Right Rock vs Left Rock (2)](https://user-images.githubusercontent.com/67421468/198841170-121f4a0f-ac11-4550-9e47-b7ebc3c152e7.png)

Setting:

![Setting (2)](https://user-images.githubusercontent.com/67421468/198841177-44e7131d-11e4-41c8-9f59-bf6a00342e22.png)

After taking 210 images for each class (It is recommended to take sufficient images in order to improve the quality of the model), the model was then trained by clicking the "Train model" button under the "Training" section. Once the model is trained the output can be tested under the "Preview" section.

![Preview](https://user-images.githubusercontent.com/67421468/198875026-b92c1b02-6546-4983-95c9-0fe2ea13d1d6.png)

After testing the output, we can export the model by clicking the "Export Model" button on the right-hand side of the page; this will create 2 files corresponding to the dataset, 'keras_model.h5'(the model) and 'labels.txt'(the parameters), which will be essential for us to be able to create the game in Python.

![Teachable Machine](https://user-images.githubusercontent.com/67421468/198841187-b8cf4106-3124-4534-a2fd-ad9e98210ed6.png)

## Setting up the environment

In order to create the model, we first need to install the libraries that the model will depend on, via the terminal (Git Bash is the best option if Windows is your operating system). In order to keep dependencies required by different projects separate, we ought to create a virtual environment.

The libraries in question are: opencv-python, tensorflow, and ipykernel.

The steps for creating the environment and installing the libraries are as follows:

1) conda create -n new-env (new_env is the name of the environment you want to create.)
2) conda activate new-env (We need to activate the environment before we can use it.)
3) conda install pip (We will need pip in order to install the packages, but in order to use pip, we will need to install it first.)
4) pip install opencv-python
5) pip install tensorflow
6) pip install ipykernel

## Creating the manual version

The 'manual_rps.py' contains the required code to create a manual version of 'Rock, Paper, Scissors'. In order to make the game, a class has been used, RPS.

Below are the features:

1 - Parameters:
    options_list - The list of gestures that will be used to play the game.

2 - Attributes:
    options_list - We are creating this as an attribute so that it can be used within a method later;
    computer_choice - str, the gesture to be played by the computer, picked randomly from options_list;
    user_choice - str, the gesture to be played by the user via input;
    winner - str, the winner of the game.

3 - Methods:
    get_computer_choice(computer_choice) - gets the computer's input;
    get_user_choice(user_choice) - gets the user's input;
    get_winner(computer_choice, user_choice, winner) - returns the winner.

Within the get_winner method, the logic of the game has been created with the use of if-elif-else statements. The statements are as follows:

![manual rps logic](https://user-images.githubusercontent.com/67421468/198841221-5e5c3935-1a31-4a10-8d08-944f0f015a1c.png)

## Creating the camera version

With this version, we will be getting the user's move with the use of the webcam. Essentially, the user is prompted to show a hand gesture to the camera, and with the use of 'keras.model.h5' the machine will guess the gesture.

### get_prediction()

In the manual version of the game, only one method was used, get_user_choice, which incorporated the input() function of the user_choice attribute to obtain the player's chosen gesture via text:

![get_user_choice](https://user-images.githubusercontent.com/67421468/198841232-a48b3bc0-4a45-419a-8dcf-3cfaaed802fd.png)

However, in order to be able to involve the webcam in the game, this code alone won't be sufficient. 3 methods will be used to obtain the user input:
    get_camera() - turns on the camera;
    get_prediction() - understands the user input with the use of 'keras_model.h5' and probabilities;
    get_user_choice() - uses the probabilities generated by get_prediction() and picks the class with the highest probability.

### Additional methods used

In a regular game, you usually count down to zero, and at that point you show your hand. As a result, in order to make the game as close to real life as possible, I have also created a get_countdown method. This slows down the machine to provide a more user_friendly experience, asking the user to prepare to show their hand.

![get_countdown](https://user-images.githubusercontent.com/67421468/198841253-4248b1dd-fdd9-40a3-be34-2e52e1edb2e0.png)

## Improvements to consider for next time

The data used to create the dataset is such that the model is only likely to perform well if I am the user. If people of a different gender or ethnicity were to try and play the game, the results will most likely be unsatisfactory.

However, for the sake of a small-scale project, I would still recommend doing such a project where multiple variables can be taken into consideration when creating a model, like I have done, as it can still teach a lot about ways to reduce overfitting issues.



