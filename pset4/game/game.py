#this is a game whereby you guess a number, you win if you guess the randomized number!

#import random
import random

import sys



#loop until positive integer from user
while True:
    try:
        level = int(input("Level: "))
        if level >0:
                break
    except ValueError:
        continue

#generate random int and compare random int to input with if statements

x = random.randint(1, level)


while True:
    try:
        guess = int(input("Guess: "))
        if guess >0:
            if guess == x:
                print("Just right!")
                break

            elif guess > x:
                print("Too large!")

            elif guess < x:
                print("Too small!")


    except ValueError:
        continue


