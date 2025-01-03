# Dictionary for the inventory
inventory = {
    # Each product will also be of type dict
}

# Ensure unique ID through a variable
inventory_id = 0

# Track of sales
sales = []
total_sale = 0


def add_product():          # Add product to inventory
    global inventory_id
    print("\nADD PRODUCT TO INVENTORY")
    product_name = str(input("Name: "))
    product_price = float(input("Price: "))
    product_quantity = int(input("Quantity: "))
    product_category = input("Category: ")

    inventory[inventory_id] = {
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity,
        "category": product_category
    }
    inventory_id += 1
    print("Product added to inventory successfully.")
    return


def view_inventory():       # View the inventory
    print("\nPRODUCT LISTING")
    if len(inventory) == 0:
        print("No items added to inventory")  # Empty inventory check
        return
    for item in inventory:
        product = inventory[item]
        print(f"""\n{item+1}. {product["name"]} (Category: {product["category"]})
                \t ID: {item}
                \t Quantity: {product["quantity"]} Pcs
                \t Price: {product["price"]} / Pc""")
    return


def sell_product():         # Sell product
    global total_sale
    print("\nSELL PRODUCT")
    if len(inventory) == 0:
        print("No products to sell")
        return
    try:
        product_id = int(input("Enter Product ID: "))
        if product_id not in inventory:
            print("Invalid Product ID. Product not found.")
            return
        original_quantity = inventory[product_id]["quantity"]
        if original_quantity == 0:
            print("This product is out of stock.")
            return
        quantity = int(
            input(f"Enter quantity to sell (max: {original_quantity}): "))
        if quantity <= original_quantity:
            inventory[product_id]["quantity"] -= quantity
            sale_report = {
                "id": product_id,
                "quantity": quantity,
                "price": quantity * inventory[product_id]["price"]
            }
            sales.append(sale_report)
            total_sale += quantity * inventory[product_id]["price"]
            print("Product sold!")
        else:
            print("Quantity to sell exceeds stock!")
    except ValueError:
        print("Invalid input. Please enter a valid Product ID or quantity.")
    return


def restock_product():       # Restock product
    print("\nRESTOCK PRODUCT")
    if (len(inventory) == 0):
        print("No products added to restock.")
        return
    try:
        product_id = int(input("Enter Product ID: "))
        if product_id not in inventory:
            print("Product not found.")
            return
        quantity = int(input("Enter quantity to restock: "))
        if quantity <= 0:
            print("Invalid restock value.")
            return
        inventory[product_id]["quantity"] += quantity
        print(f"""Product restocked successfully. New quantity: {
              inventory[product_id]['quantity']}""")
    except ValueError:
        print("Invalid input. Please enter a valid Product ID or quantity.")
    return


def delete_product():        # Delete product from inventory
    print("\nDELETE PRODUCT")
    if (len(inventory) == 0):
        print("No products to delete.")
        return
    try:
        product_id = int(input("Enter Product ID to delete: "))
        if product_id not in inventory:
            print("Product not found.")
            return
        del inventory[product_id]
        print(f"Product with ID {product_id} deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid Product ID.")
    return


def modify_product():        # Modify existing product details
    print("\nMODIFY PRODUCT DETAILS")
    if (len(inventory) == 0):
        print("No products added to modify.")
        return
    try:
        product_id = int(input("Enter Product ID to modify: "))
        if product_id not in inventory:
            print("Product not found.")
            return
        product_name = input(
            f"Enter new name (current: {inventory[product_id]['name']}): ")
        product_price = float(input(
            f"Enter new price (current: {inventory[product_id]['price']}): "))

        product_quantity = int(input(f"""Enter new quantity (current: {
                                 inventory[product_id]['quantity']}): """))

        product_category = input(f"Enter new category (current: {
                                 inventory[product_id]['category']}): ")

        inventory[product_id] = {
            "name": product_name,
            "price": product_price,
            "quantity": product_quantity,
            "category": product_category
        }
        print("Product details updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid Product ID.")
    return


def generate_sales_report():  # Generate sales report
    print("\nSALES REPORT")
    global total_sale
    quantity = 0
    for sale in sales:
        quantity += sale["quantity"]
        product_name = inventory[sale["id"]]["name"]
        print(f"""Sold {sale['quantity']} of {
              product_name} for ${sale['price']}""")
    print(f"Total items sold: {quantity}")
    print(f"Total sales revenue: {total_sale}")
    return


def pause():                  # Helper function to pause after execution of a certain module
    input("Press any key to continue")
    return


def main():     # Main program flow
    while True:
        print("\nWELCOME TO INVENTORY MANAGEMENT SYSTEM\n")
        print("1. Add product to inventory")
        print("2. Display inventory")
        print("3. Sell product")
        print("4. Restock product")
        print("5. Delete product from inventory")
        print("6. Modify product details")
        print("7. Generate sales report")
        print("\nType 0 to exit")

        try:
            opt = int(input("Enter the corresponding number: "))
            if opt == 1:
                add_product()
                pause()
            elif opt == 2:
                view_inventory()
                pause()
            elif opt == 3:
                sell_product()
                pause()
            elif opt == 4:
                restock_product()
                pause()
            elif opt == 5:
                delete_product()
                pause()
            elif opt == 6:
                modify_product()
                pause()
            elif opt == 7:
                generate_sales_report()
                pause()
            elif opt == 0:
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            pause()


# Call the main program flow
main()


# Old test cases:

'''
add_product()
add_product()
view_inventory()
sell_product()
restock_product()
view_inventory()
generate_sales_report()
'''
