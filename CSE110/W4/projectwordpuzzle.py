# Project World Puzzle
# Creative Addition: Added a maximum lives limtit system. If the user runs out of lives, the game ends and reveals the secret word.

answer = "mosiah"
count = 0
max_lives = 6 #Total number of lives/chances permited

print("Welcome to the word puzzle!")
print(f"You have {max_lives} lives to guess the secret word!")

initial_hint = ""
for letter in answer:
      initial_hint += "_ "

hint = initial_hint
guess = ""

while guess != answer:
      lives_left = max_lives - count 
      print(f"Lives remaing: {lives_left}")
      print(f"Your hint is: {hint}")
      guess = input("What is your guess? ").lower()
      count += 1

      if guess == answer or count >= max_lives:
           break
      elif len(guess) != len(answer):
         print("Sorry, the guess must have the same number of letters as the secret word.")
      else:
         new_hint = ""
         for i in range(len(answer)):
              if guess[i] == answer[i]:
                   new_hint += guess[i].upper() + " "
              elif guess[i] in answer:
                   new_hint += guess[i].lower() + " "
              else:
                   new_hint += "_ "
         hint = new_hint
         print("Your guess was not correct.")

if guess == answer:
     print("Congratulations! You guessed it!")
     print(f"It took you {count} guesses.")
else:
     print("Game Over! You ran out of lives!")
     print(f"The secret word was: {answer}.")