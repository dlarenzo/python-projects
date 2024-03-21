import random

random_side= random.randint(0,1)

# since we know the random number is either 0 or 1, we can use a conditional to determine the outcome
if random_side == 1:
  print("Heads")
else:
  print("Tails")
  
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Icaco", "Jujube", "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tangerine", "Ugli", "Vanilla", "Watermelon", "Xigua", "Yellow watermelon", "Zucchini"]