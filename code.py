# number guessing game
import random
randomV = random.randrange(1, 100)
while(True):
    str1 = int(input("Guess any number from 1 to 100:     "))
    if(str1 == randomV):
        print("You guess the correct number.")
        break
    else:
        print("You guess the wrong number.")
        print(f"The number is {randomV}.")
        print("Try to guess the right number again.")
        randomV = random.randrange(1, 100)
