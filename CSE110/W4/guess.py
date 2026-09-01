#Guess My Number Game!
import random 

keep_playing = "yes"

while keep_playing == "yes":
    secrect_number = random.randint(1,100)

    guess_count = 0
    guess = -1

    while guess != secrect_number:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1 

        if guess < secrect_number:
            print("Higher")
        elif guess > secrect_number:
            print("Lower")
        else:
            print("You guessed it!")

    print(f"It took you {guess_count} guesses") 

    keep_playing = input("would you like to play again (yes/no)? ")

keep_playing = "no"
print("Thank you for playing. Goodbye!")