def creditval(num):
    # Convert the number to a list of integers
    list_num = [int(digit) for digit in num]
    new_list = []

    # Start from the second to last digit and move backwards
    for index, digit in enumerate(reversed(list_num)):
        if index % 2 == 1:  # Double every second digit
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            new_list.append(doubled)
        else:
            new_list.append(digit)

    # Calculate the sum of the processed numbers
    lisum = sum(new_list)

    # Check if the total modulo 10 is 0
    if lisum % 10 == 0:
        print("Credit card is valid")
    else:
        print("Error, credit card invalid")


credit = input('Enter Credit card number: ')  # Keep as a string to maintain leading zeros
creditval(credit)


# Simple inventory
def display_menu():
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item Quantity")
    print("4. Remove Item")
    print("5. Exit")


def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")


def add_item(inventory):
    item = input("Enter the item name to add: ").strip()
    category = input("Which category ").strip()
    if item in inventory[item]:
        print(f"{item} already exists in inventory with quantity {inventory[item]}.")
    else:
        try:
            quantity = int(input(f"Enter the quantity of {item}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[item] = quantity
                print(f"Added {item} with quantity {quantity}.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")


def update_item_quantity(inventory):
    item = input("Enter the item name to update: ").strip()
    if item not in inventory:
        print(f"{item} does not exist in inventory.")
    else:
        try:
            quantity = int(input(f"Enter the new quantity of {item}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[item] = quantity
                print(f"Updated {item} to quantity {quantity}.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")


def remove_item(inventory):
    item = input("Enter the item name to remove: ").strip()
    if item in inventory:
        del inventory[item]
        print(f"Removed {item} from inventory.")
    else:
        print(f"{item} does not exist in inventory.")


def main():
    inventory = {
        'Product prices': {
        },
        'Quantity threshold': {
        },
        'Product categories': {
        },
        'Sales': {
        }
    }

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            view_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            update_item_quantity(inventory)
        elif choice == '4':
            remove_item(inventory)
        elif choice == '5':
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
