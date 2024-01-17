class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print("Ok!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Number: {self.contacts[name]}")
        else:
            print("Contact not found.")

# Function to display the menu and get user input
def get_user_command():
    print("Command (1 search, 2 add, 3 quit):")
    return int(input())

# Main phone book application
phone_book = PhoneBook()

while True:
    command = get_user_command()

    if command == 1:
        # Search
        name_to_search = input("Enter the name to search: ")
        phone_book.search_contact(name_to_search)
    elif command == 2:
        # Add
        name_to_add = input("Enter the name: ")
        number_to_add = input("Enter the number: ")
        phone_book.add_contact(name_to_add, number_to_add)
    elif command == 3:
        # Quit
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please enter 1, 2, or 3.")
