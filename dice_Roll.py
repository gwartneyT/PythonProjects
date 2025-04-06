# This is the dice rolling exercise. The goal is to make a 2 int RNG 
# Additionally, add a total roll counter and the option to change the total number of dice.   
elif choice == "r":
        input("Roll the dice? (y/n): ").lower()

# Example code below
import random   #Import function and random module.

while True:   #Begins loop of code below
    choice = input("Roll the dice? (y/n): ").lower()   # Define choice as input string
    if choice == "y": 
        die1 =random.randint(1, 6)   # Generate random integer (randint) btwn 1 and 6 (inclusive).
        die2 = random.randint(1, 6)

        print(f"({die1}, {die2})")   #Die1 and die2 inserting to fstring (use curly brackets for this).
        print(f"Total Roll is... {die1 + die2}.")   #Contain function of d1 + d2 in curly brackets.
    elif choice == "n":   # "Else/If" function. (elif for SECOND function in sequence or first will not run.
        print("Fuck!")
        break   #Break functions stops loop. 
    else:   #If anything other than Y or N is typed;
        print("Invalid!")
