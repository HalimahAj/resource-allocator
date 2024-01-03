import pandas as pd

# Creating the Resource class
class Resource:
    # Initializing
    def __init__(self, name, quantity):
    # Attributes of the Resource class
        self.name = name
        self.quantity = quantity
        self.available_quantity = quantity

    # Defining functions/methods

    # to allocate resources
    def allocate(self, quantity):
        if quantity <= self.available_quantity:
            self.available_quantity -= quantity
            print(f'{quantity} {self.name} allocated. {self.available_quantity} available.')
        else:
            print(f'Not enough {self.name} available. Available quantity is {self.available_quantity}')

    # to deallocate resources
    def deallocate(self, quantity):
        self.available_quantity += quantity



# Creating the Inventory class
class Inventory:
    # Initializing
    def __init__(self):
        self.inventory = []

    # Defining functions/methods

    # adding resources to the inventory
    def add_resource(self, name, quantity):
        resource = Resource(name, quantity)
        self.inventory.append(resource)

    # to display information about a resource
    def display_resource_information(self):
        print("\nResource Information:")
        for resource in self.inventory:
            print(f"- {resource.name}: {resource.available_quantity} available")

    # to find a resource in the inventory
    def find_resource(self, resource_name):
        for resource in self.inventory:
            if resource.name == resource_name:
                return resource
        return None

    # Creating a DataFrame to store all resource information
    def all_resources(self):
        data = {"Name": [resource.name for resource in self.inventory],
                "Available Quantity": [resource.available_quantity for resource in self.inventory]}
        df = pd.DataFrame(data)
        return df


    # defining a menu for users to make a choice
    def show_menu():
        print("*" * 50)
        print("Menu:")
        print("1. Add resource")
        print("2. Allocate resource")
        print("3. Deallocate resource")
        print("4. Exit")
        print("*" * 50)

    # getting an input from the user
    def get_user_choice():
        choice = int(input("Enter your choice (1-4): "))
        if 1 <= choice <= 4:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    # defining action to take depending on user choice
    def perform_action(choice):
        # if choice is to add resource
        if choice == 1:
            resource_name = input("Enter resource name: ")
            resource_quantity = int(input("Enter resource quantity: "))
            inventory.add_resource(resource_name, resource_quantity)
        # if choice is to allocate resource
        elif choice == 2:
            resource_name = input("Enter resource name to allocate: ")
            resource_quantity = int(input("Enter quantity to allocate: "))
            resource = inventory.find_resource(resource_name)
            if resource:
                resource.allocate(resource_quantity)
            else:
                print(f"{resource_name} not found in inventory.")
        # if choice is to deallocate resource
        elif choice == 3:
            resource_name = input("Enter resource name to deallocate: ")
            resource_quantity = int(input("Enter quantity to deallocate: "))
            resource = inventory.find_resource(resource_name)
            if resource:
                resource.deallocate(resource_quantity)
            else:
                print(f"{resource_name} not found in inventory.")
        # if exiting
        elif choice == 4:
            print("Exiting, \n Thank you")


# Creating an instance of the Inventory class
inventory = Inventory()

# Running the menu
while True:
    Inventory.show_menu()
    user_choice = Inventory.get_user_choice()
    Inventory.perform_action(user_choice)
    if user_choice == 4:
        break

# Displaying resource information after menu execution
inventory.display_resource_information()

# Displaying all resources as a DataFrame
all_resources_df = inventory.all_resources()
print("\nAll Resources:")
print(all_resources_df)
