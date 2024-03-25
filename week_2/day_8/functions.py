# REMINDER OF WHAT A FUNCTION LOOKS LIKE

# DEF MY_FUNCTION():
#     # DO THIS 
#     # DO THAT
#     # FINALLY DO THIS

# CALL FUNCTION
# MY_FUNCTION()

#FUNCTION WITH NO INPUT (PARAMETERS)
def greet():
    print("Hello, World!")
    print("How are you today?")
    print("I hope you are doing well!")
greet()

# LET'S ADD A PARAMETER TO OUR FUNCTION
# DEF MY_FUNCTION(SOMETHING PARAMETER):
#     # DO THIS WITH SOMETHING
#     # DO THAT WITH SOMETHING
#     # FINALLY DO THIS WITH SOMETHING

# CALL FUNCTION
# MY_FUNCTION(SOMETHING ARGUMENT)

#FUNCTION WITH ONE INPUT (PARAMETER)
def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How are you today, {name}?")
    print(f"I hope you are doing well, {name}!")
    
greet_with_name("LaRenzo")


#FUNCTION WITH ONE INPUT (PARAMETER)
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")
    print(f"I hope you are doing well, {name}!")

greet_with("LaRenzo", "New York")