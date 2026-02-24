# We are going to write a program that generates a random number and asks the user to guess it,
# If the player's guess is higher than the actual number, the program display "lowev number please."
# Similarly if the user's guess is too low, the program prints "higher number please"
# When the user guess the correct number, the program display the number of guesses the player used to arrive at the number.

# Hint : Use The Random Module

import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):

    userGuess = int(input("Enter Your Guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You Guessed It Right!")

    else:
        if(userGuess>randNumber):
            print("You Guessed It Wrong! Enter A Smaller Number")
        else:
            print("You Guessed It Wrong! Enter A Larger Number")    

print(f"You Guessed The Number in {guesses} Guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))