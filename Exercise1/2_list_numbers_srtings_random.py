import random


# Function to get user input for a list of numbers
def get_user_numbers():
    numbers = [int(input("Enter a number: ")) for _ in range(10)]
    return numbers


# Function to get user input for a list of strings
def get_user_strings():
    strings = [input("Enter a string: ") for _ in range(10)]
    return strings


# Function to generate a list of random numbers
def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    return random_numbers


# Main program
user_numbers = get_user_numbers()
user_strings = get_user_strings()
random_numbers = generate_random_numbers()

# Format the output with square brackets and single quotes
formatted_user_numbers = [str(num) for num in user_numbers]
formatted_user_strings = ['' + s + '' for s in user_strings]
formatted_random_numbers = [str(num) for num in random_numbers]

print("Integers:", formatted_user_numbers)
print("Strings:", formatted_user_strings)
print("Random Numbers:", formatted_random_numbers)
