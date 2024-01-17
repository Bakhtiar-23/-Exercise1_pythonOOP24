import random

# Function to roll a six-sided dice
def roll_dice():
    return random.randint(1, 6)

# Example of calling the function and printing the result
result = roll_dice()
print(f"The result of rolling the dice is: {result}")
