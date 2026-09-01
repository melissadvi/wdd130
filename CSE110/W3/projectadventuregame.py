#Project: Adventure Game 
#Creative Description: I added a magical cave themed after the "One Piece" anime.
#I also tested this game with two of my friends and they really enjoyed the game and the anime reference!

# First Scenario: Start Of The Game
first = input("You find two items: a MATCH and a FLASHLIGHT. Do you want to pick up one of them or just LEAVE? ").lower()

# Pathway if choose MATCH
if first == "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. " \
    "You see a large grizzly bear, and the match burns out.") #Level 1 Response

    second = input("Do you want to RUN or HIDE behind a tree? ").lower() #Level 2 Question 

    if second == "run": #Level 3 if choose RUN 
        run = input("The grizzly bear chases you! Do you want to climb a TREE or jump into the RIVER? ").lower()
        if run == "tree":
            print("The bear cannot climb thin trees. You are safe! You can continue your journey!")
        elif run == "river":
            print("The river current was too strong. Game over!")
        else:
            print("Sorry, this is not possible.")
            
    elif second == "hide": #Level 3 if choose HIDE
        hide = input("The bear loses your scent. Do you want to WALK back to the road or SLEEP under the tree? ").lower()
        if hide == "walk":
            print("You are safe now. You can continue your journey!")
        elif hide == "sleep":
            print("It gets too cold during the night. Game over!")
        else:
            print("Sorry, this is not possible.")
    else:
        print("Sorry, this is not possible.")

# Pathway if choose FLASHLIGHT
elif first == "flashlight":
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you " \
       "thought you also heard something off to the side.") #Level 1 Response

    third = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ").lower() #Level 2 Question
        
    if third == "follow": #Level 3 if choose FOLLOW + Creative Part: Magical Cave
        print("You follow the path and find the mysterious magic cave!!") 

        follow = input("Do you want to ENTER the magical cave or CONTINUE walking into the forest? ").lower()
        if follow == "enter":
           print("Inside the magical cave, you find the One Piece treasure! You win!") 
        elif follow == "continue":
            print("You keep walking, but you get lost in the dark. Game over.")
        else:
            print("Sorry, this is not possible.")

    elif third == "look": #Level 3 if choose LOOK
        print("You shine your light into the trees and find the grizzly bear looking right at you!")
        
        look = input("Do you want to BLIND the bear with your light or SCREAM for help? ").lower()
        if look == "blind":
            print("The bear is stunned! You can run away and continue your journey!")
        elif look == "scream":
            print("Your screams made the bear even more angry and it attacks you. Game over!")
        else: 
            print("Sorry, this is not possible.")
    else:
        print("Sorry, this is not possible.")

# Pathway if choose LEAVE
elif first == "leave":
    print("You decide to leave both items behind and walk away in the forest.") #Level 1 Response

    fourth = input("You hear howling in the distance. Do you want to run BACK or walk SLOWLY? ").lower() #Level 2 Question

    if fourth == "back": #Level 3 if choose BACK
        back = input("You trip on a rock! Do you want to CRAWL into a bush or try to STAND UP? ").lower()
        if back == "crawl":
            print("You hid successfully until morning. You survived and can continue your journey!")
        elif back == "stand up":
            print("You hurt your ankle and couldn't escape. Game over!")
        else:
            print("Sorry, this is not possible.")

    elif fourth == "slowly": #Level 3 if choose SLOWLY
        slowly = input("A wolf blocks your path! Do you want to FIGHT with a stick or climb a ROCK? ").lower()
        if slowly == "fight":
            print("The wolf was too strong. Game over!")
        elif slowly == "rock":
            print("Wolves can't climb rocks. You wait them out and survive! You can continue your journey!")
        else:
            print("Sorry, this is not possible.")

# If the user enters wrong at the first question
else: 
   print("Sorry, this is not possible.")