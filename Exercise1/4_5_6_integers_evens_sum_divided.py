# Function to read integers from the user until 0 is entered
def read_integers():
    integers = []
    while True:
        num = int(input("Enter an integer: "))
        if num == 0:
            break
        integers.append(num)
    return integers

# Function to count the number of negative integers
def count_negative_integers(numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count

# Function to count the number of even integers
def count_even_integers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Function to count the sum of positive integers divisible by three
def sum_positive_divisible_by_three(numbers):
    total = 0
    for num in numbers:
        if num > 0 and num % 3 == 0:
            total += num
    return total

# Main program
print("Enter integers until enter 0 to stop.")

# Read integers from the user
user_integers = read_integers()

# Count the number of negative integers
negative_count = count_negative_integers(user_integers)

# Count the number of even integers
even_count = count_even_integers(user_integers)

# Sum of positive integers divisible by three
sum_positive_divisible_by_three_result = sum_positive_divisible_by_three(user_integers)

# Print the results
print(f"Number of negative integers: {negative_count}")
print(f"Number of even integers: {even_count}")
print(f"Sum of positive integers divisible by three: {sum_positive_divisible_by_three_result}")
