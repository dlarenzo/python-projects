# Ceasar Cipher.  Method to encode and decode messages. You shift the letters by a number of positions. This will shift what the letter is. A is A, but if you shift it by 1, it becomes B.
# 

# ALPHABET
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# BASE CODE.  MESSAGES FOR WHAT TO DO

message = input("Type your message:\n")

shift_number = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print (f"Here's the {cipher_direction}d result: {end_text}")
      
# ENCODE FUNCTION
# CREATE A FUNCTION CALLED ENCRYPT THAT TAKES THE MESSAGE AND SHIFT AS INPUTS

# INSIDE THE ENCRYPT FUNCTION, SHIFT EACH LETTER OF THE 'MESSAGE' FORWARDS IN THE ALPHABET BY THE SHIFT AMOUNT AND PRINT THE ENCRYPTED TEXT.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

# THE CAESAR FUNCTION TAKES IN BOTH THE ENCRYPT AND DECRYPT FUNCTIONS SO THE TWO FUNCTIONS BELOW ARE COMMENTED OUT
# def encrypt(plain_message, shift_amount):
#   #CREATE AN EMPTY STRING CALLED CIPHER_TEXT
#   cipher_message = ""
#   # START OFF WITH FOR LOOP AND LOOP THROUGH THE LETTERS IN THE PLAIN_MESSAGE
#   for letter in plain_message:
#   #FIND OUT PLACEMENT OF ALPHABET LETTERS BY USING INDEX FUNCTION. save it into a variable called position
#     position = alphabet.index(letter)
#   #CREATE NEW POSITION AND MAKE IT EQUAL TO POSITION PLUS SHIFT AMOUNT. NEW LETTER WILL BE EQUAL TO ALPHABET AT NEW POSITION. CIPHER MESSAGE WILL BE PLUS EQUAL TO NEW LETTER
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_message += new_letter
#   results = print (f"Here's the encoded result: {cipher_message}")

# # CALL THE ENCRYPT FUNCTION AND PASS IN THE USERS INPUTS. YOU SHOULD BE ABLE TO TEST THE CODE AND SEE THE ENCODED MESSAGE.
# encrypt(plain_message=message, shift_amount=shift_number)

# # DECODE FUNCTION
# # CREATE A FUNCTION CALLED DECRYPT THAT TAKES THE DECIPHERS MESSAGE
# def decrypt(cipher_text, shift_amount):
#   decipher_message = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     new_letter = alphabet[new_position]
#     decipher_message += new_letter
#   results = print (f"Here's the decoded result: {decipher_message}")
  

# CAESAR FUNCTION TAKES CARE OF THE IF ELIF STATEMENTS FOR ENCRYPT AND DECRYPT SO THE TWO FUNCTIONS BELOW ARE COMMENTED OUT
# if direction == "encode":
#   encrypt(plain_message=message, shift_amount=shift_number)
# elif direction == "decode":
#   decrypt(cipher_text=message, shift_amount=shift_number)
  
# cipher_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")

# if cipher_again == "yes":
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   message = input("Type your message:\n")
#   shift_number = int(input("Type the shift number:\n"))
#   if direction == "encode":
#     encrypt(plain_message=message, shift_amount=shift_number)
#   elif direction == "decode":
#     decrypt(cipher_text=message, shift_amount=shift_number)
# else:
#   print("Translation Complete.\n Goodbye")
  
caesar(start_text=message, shift_amount=shift_number, cipher_direction=direction)
  


