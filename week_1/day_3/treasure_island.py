print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# print You're at a cross road.  Where do you want to go? Type "left" or "right"
cross_roads = input("You're at a cross road.  Where do you want to go? Type 'left' or 'right' ")

# if right print: You went right and fell into an endless hole. Game Over.
#if left print: You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
if cross_roads == "right":
  print("You went right and fell into an endless hole. Game Over.")
else:
  swim_wait = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")

# if swim print: While swimming you we attacked by a gang of ferocious fish. Game Over.
# if wait print: You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?   
  if swim_wait == "swim":
    print("While swimming you we attacked by a gang of ferocious fish. Game Over.")
  else:
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
  
# if wait print: You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
# if red print: It's a room full of fire. Game Over. Guess that burned LOL!
# if yellow print: You found the treasure! You Win!
# if blue print: You enter a room of beasts. You were eaten! Game Over.  Guess we didn't need to know where to find those Fantastic Beasts LOL! Too soon?    
    if door == "red":
      print("It's a room full of fire. Game Over. Guess that burned LOL!")  
    elif door == "blue":
      print("You enter a room of beasts. You were eaten! Game Over.  Guess we didn't need to know where to find those Fantastic Beasts LOL! Too soon?")
    else: 
      print("You found the treasure! You Win!")
    
        
    # else:
    #     print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    #     door = input()
    #     if door == "red":
    #         print("It's a room full of fire. Game Over. Guess that burned LOL!")
    #     elif door == "yellow":
    #         print("You found the treasure! You Win!")
    #     else:
    #         print("You enter a room of beasts. You were eaten! Game Over.  Guess we didn't need to know where to find those Fantastic Beasts LOL! Too soon?")

