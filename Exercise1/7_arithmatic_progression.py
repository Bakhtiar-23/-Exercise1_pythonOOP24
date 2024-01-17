# Function to process the arithmetic progression
def process_arithmetic_progression(max_value):
    terms = [i for i in range(3, max_value + 1, 3)]
    num_terms = len(terms)
    sum_of_terms = sum(terms)
    sum_of_squared_terms = sum(x**2 for x in terms)
    return num_terms, sum_of_terms, sum_of_squared_terms, terms

# Get the maximum value from the user
max_value = int(input("Give maximum value: "))

# Check if max_value is at least 3
if max_value < 3:
    print("Error: The maximum value must be at least 3.")
    print("Procession is: 0")
    print("Number of terms is: 0")
    print("Sum of terms is: 0")
    print("Sum of squared terms is: 0")

else:
    # Process the arithmetic progression
    num_terms, sum_of_terms, sum_of_squared_terms, ap_terms = process_arithmetic_progression(max_value)

    # Print the arithmetic progression
    print(f"Procession is: {', '.join(map(str, ap_terms))}")

    # Print the results
    print(f"Number of terms is: {num_terms}")
    print(f"Sum of terms is: {sum_of_terms}")
    print(f"Sum of squared terms is: {sum_of_squared_terms}")
