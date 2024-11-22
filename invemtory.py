def display_menu():
    print('\n Inventory Management System')
    print('1. View inventory')
    print('2. Add product')
    print('3. Remove product')
    print('4. Search for product')
    print('5. Exit')

def view_inventory(inventory):
    if not inventory:
        print('Inventory not found')
    else:
        print('\n Current inventory: ')
        for items, quantity in inventory.items():
            print(f'{items}:{quantity}')

def add_product(inventory):
    product = input('\n Please enter the name of the product: ').strip()
    category = input('Please enter the product category: ').strip()

    if category not in inventory['category']:
        inventory['category'][category] = []

    if product in inventory['category'][category]:
        print(f'{product} already exists. Would you like to add its quantity or change its price?')
    else:
        inventory['category'][category].append(product)

        try:
            quantity = int(input("Enter the quantity of the product: ").strip())
            if quantity < 0:
                print('Quantity cannot be negative')
            else:
                inventory['quantity'][product] = quantity
                print(f"Quantity has been updated to {quantity}")

            price = float(input("Enter the price: ").strip())
            if price < 0:
                print("Are we on promo?")
            else:
                inventory['price'][product] = price
                print('The price has been updated')
        except ValueError:
            print("Invalid entry, please enter a valid number for quantity or price.")
1
def remove_product(inventory):
    product = input("Enter product to remove: ").strip()
    category = input("Which category ").strip()
    if product in inventory["category"][category]:
        del inventory['category'][category]
        if product in inventory['price']:
            del inventory['price'][product]
            if product in inventory['quantity']:
                del inventory['quantity'][product]
    else:
        print(f'{product} does not exist')

def search(inventory):
    product = input("Enter the product to search for: ").strip().lower()
    category = input('Enter category: ').strip().lower()

    # Check if category exists
    if category not in inventory['category']:
        print(f"Category '{category}' does not exist.")
        return

    # Search for the product in the specified category
    found_product = None
    for item in inventory['category'][category]:
        if product in item.lower():  # Case-insensitive, partial match
            found_product = item
            break

    if found_product:
        # Display product information
        print(f"\nProduct Found in Category '{category.capitalize()}':")
        print(f"Product Name: {found_product}")
        print(f"Price: {inventory['price'][found_product]}")
        print(f"Quantity: {inventory['quantity'][found_product]}")
    else:
        print(f"'{product}' does not exist in the category '{category}'.")



inventory = {
        'category' : {},
        'price' : {},
        'quantity' : {}
    }

while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            view_inventory(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            remove_product(inventory)
        elif choice == '4':
            search(inventory)
        elif choice == '5':
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    print("ready")






