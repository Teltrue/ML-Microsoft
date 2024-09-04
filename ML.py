def display_menu():
    print('\n Inventory Management System')
    print('1. View inventory')
    print('2. Add product')
    print('3. Remove product')
    print('4. Search for product')

def view_inventory(inventory):
    if not inventory:
        print('Inventory not found')
    else:
        print('\n Current inventory: ')
        for items, quantity in inventory.items():
            print(f'{items}:{quantity}')
            
def add_producct(inventory):
    product = input('\n Please enter the name of the product').strip()
    category = input('Please enter the products category')
    
