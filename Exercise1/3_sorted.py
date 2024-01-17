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

# Sort numbers and strings
sorted_user_numbers = sorted(user_numbers)
sorted_user_strings = sorted(user_strings)
sorted_random_numbers = sorted(random_numbers)
# Format the output with square brackets and single quotes
formatted_user_numbers = [str(num) for num in sorted_user_numbers]
formatted_user_strings = ['' + s + '' for s in sorted_user_strings]
formatted_random_numbers = [str(num) for num in sorted_random_numbers]

print("Sorted Integers:", formatted_user_numbers)
print("Sorted Strings:", formatted_user_strings)
print("Sorted Random Numbers:", formatted_random_numbers)
