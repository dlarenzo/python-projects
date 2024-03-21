import random

#Step 1
word_list = ["aardvark", "baboon", "camel"]

# TODO - 1 - RANDOMLY SELECT A WORD FROM THE WORD LIST AND ASSIGN IT TO A VARIABLE CALLED CHOSEN_WORD.
chosen_word =random.choice(word_list)

# TEST CODE - Don't keep in final submission, this is just to know what word was chosen
print(f"Chosen word is: {chosen_word}")

# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 underscores

display = []
for letter in chosen_word:
    display.append("_")
    
print(display) # Don't keep in final submission, this is just to test the code

# TODO - 2 - ASK THE USER TO GUESS A LETTER AND ASSIGN THEIR ANSWER TO A VARIABLE CALLED GUESS. MAKE GUESS LOWERCASE.
guess = input("Guess a letter: ").lower()


# LOOP THROUGH EACH POSITION IN THE CHOSEN_WORD;
# IF THE LETTER AT THAT POSITION MATCHES 'GUESS', THEN REPLACE THAT POSITION IN THE DISPLAY WITH 'GUESS'.

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display) # Don't keep in final submission, this is just to test the code
  

# TODO-3 - CHECK IF THE LETTER THE USER GUESSED (GUESS) IS ONE OF THE LETTERS IN THE CHOSEN_WORD.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        
        
