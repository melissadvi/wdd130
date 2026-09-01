men = int(input("How many men are there? "))
women = int(input("How many women are there? "))

total = men + women 

has_enough_players = total >= 7
has_enought_women = women >=4

if has_enough_players and has_enought_women:
   print("You can play!")
else:
   print("You cannot play a legal game")

if not has_enough_players:
   print("Ask the other team if they want to practice")
#  not first
#  and is next
#  or  is last 