#Password Generator
# Goal is to Generate a random password with the given number of letters, symbols and numbers

# Import the random module
# Import the string module to use a collection of constants representing set of charaters, like ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits, punctuation, printable, whitespace
import random 
import string

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
numb_letters = int(input("How many letters would you like in your password?\n"))
numb_symbols = int(input("How many symbols would you like?\n"))
numb_numbers = int(input("How many numbers would you like?\n"))


# EAZY LEVEL - Order not randomised:

# password = ""

# for char in range(1, numb_letters + 1):
  
#   password += random.choice(letters)
  

# for char in range(1, numb_symbols + 1):
  
#   password += random.choice(symbols)
  
  
# for char in range(1, numb_numbers + 1):
  
#   password += random.choice(numbers)
  
# print(password)


# HARD LEVEL - Order of characters randomised:

# here we won't use a password string, we will use a list [] to store the characters and then we will use the random.shuffle() method to shuffle the characters in the list (also changing password to password_list to avoid confusion with the password string above )
password_list = []

# For below you can use the += operator to add the random.choice() to the list, but you can also use the append() method to add the random.choice() to the list.  I will use the append
for char in range(1, numb_letters + 1):
  
  password_list.append(random.choice(letters))
  

for char in range(1, numb_symbols + 1):
  
  password_list.append(random.choice(symbols))
  
  
for char in range(1, numb_numbers + 1):
  
  password_list.append(random.choice(numbers))

# to shuffle the characters in the list you can use the random.shuffle() method
print(password_list)
random.shuffle(password_list)  
print(password_list)

# Let's turn password back into a string as right now each character is a separate item in the list with quotation marks around it and we don't want that

password=""
for char in password_list:
  password += char

print(f"Your password is: {password}")