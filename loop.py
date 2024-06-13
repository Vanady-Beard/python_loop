# Lesson 4: Assignments | Python Loop Statements

# 1. The Range Riddle
# Task 1: Every Other Day 

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for even_days in range(0, len(days_of_week), 2):

    print (days_of_week[even_days])

# 3. Loop Condition Logic
item = 0 

while item < 10:
    print("This iterations is on", item)
    item += 1
    
    if item == 6:
        
        break

    print (item )

#4. Python's Random Game Night
#Task 1: Random Choice Game


import random

game_items = ["chess", "scrabble", "connect four", "sorry", "clue"]
game_random = (random.choice(game_items))

while True:
    user_input = input(f"Which indoor game item was selected out of these 5 options {game_items}?")
    if user_input == game_random:
        print ("You guessed right")
        print ("End of the game")
        break

    else: 
        print ("Guess again")


    

