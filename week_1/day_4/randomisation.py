import random

random_integer = random.randint(1, 10)
print(random_integer)

# AUTOMATICALLY CHOOSES A RANDOM FLOAT BETWEEN 0.0000000000000000 AND 0.9999999999999999
# random_float = random.random()
# print(random_float)

# HOW TO CREATE A RANDOM DECIMAL NUMBER BETWEEN 0 AND 5 OR CHANGE THE 5 TO WHATEVER NUMBER YOU WANT
random_float = random.random() * 5
print(random_float)

# EXAMPLE OF USING THE RANDOM MODULE TO CHOOSE BETWEEN TWO OPTIONS FOR INTEGERS TO DO LOVE SCORE
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")