"""
Guessing Game.
Except the number is constantly changing.
Based on your guess.
"""
import random
ans = random.randint(1,100)
while True:
    num = int(input("Enter a number [1~100]:"))
    if num == ans:
        print("You got it!")
        break
    elif num > ans:
        print("Too large.")
    else:
        print("Too small.")

    random.seed(num) # Make the RNG deterministic.
                     # So that you don't suddenly win the game
                     # by repeatedly providing the same value.

    ans = random.randint(1,100) # ;P
