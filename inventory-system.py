#Assignment: Create an inventory management system - Use loops to display or update a list of stock items
stockAvailable = {
    "Prestige" : 20,
    "Softcare" : 30,
    "Nomi" : 40
}
def show_inventory():
        print("Current Stock Item : Qty ")
        for item, qty in stockAvailable.items():
            print(f">   {item} : {qty}")

def update_stock():
    item = input("\nEnter item you want to update: \n")
    if item in stockAvailable:
        qty = int(input("Enter quantity to add. \n"))
        stockAvailable[item] += qty
        print(f"{item} updated. New quantity is {stockAvailable[item]}\n")
    else:
        qty = int(input(f"{item} not found. Enter quantity of item: \n"))
        stockAvailable[item] = qty
        print(f"{item} has been added to stock available.\n")
        
while True:
    print("....Inventory Management....")
    print("1. View Inventory")
    print("2. Update Stock")
    print("3. Exit")
    
    choice = input("\nType your option(1/2/3) from the Menu\n")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        print("Exiting Inventory Management System.")
        break
    else:
        print("Invalid Option")