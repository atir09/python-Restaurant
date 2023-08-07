import json




class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

    def to_json(self):
        return {
            "snack_id": self.snack_id,
            "name": self.name,
            "price": self.price,
            "availability": self.availability
        }

# Testing the Snack class


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

snack_inventory = load_inventory()

# Defining ADD, Remove and Update Functions
def add_snack(snack):
    snack_inventory.append(snack.to_json())
    save_inventory(snack_inventory)

def remove_snack(snack_id):
    snack_inventory[:] = [snack for snack in snack_inventory if snack["snack_id"] != snack_id]
    save_inventory(snack_inventory)

def update_snack_availability(snack_id, availability):
    for snack in snack_inventory:
        if snack["snack_id"] == snack_id:
            snack["availability"] = availability
            save_inventory(snack_inventory)
            break



# Function for Maintaning Sales Records

def save_sales(sales):
    with open("sales.json", "w") as json_file:
        json.dump(sales, json_file, indent=4)

def load_sales():
    try:
        with open("sales.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []


# Function for adding the item sold in saleFile and Printing Total Sale

def record_sale(snack_id):
    for snack in snack_inventory:
        if snack["snack_id"] == snack_id and snack["availability"]:
            snack["availability"] = False
            save_inventory(snack_inventory)
            price = snack["price"]
            sale_entry = {"snack_id": snack_id, "price": price, "timestamp": str(datetime.datetime.now())}
            sales_records.append(sale_entry)
            save_sales(sales_records)
            print(f"Sale recorded. Total amount: {price} INR")
            break
    else:
        print("Invalid snack ID or snack is not available.")


def get_snack_details():
    snack_name = input("Enter snack name: ")
    price = float(input("Enter price (INR): "))
    availability = input("Is the snack available (yes/no): ").lower() == "yes"
    return snack_name, price, availability

def main():
    while True:
        print(snack_inventory)
        print("Welcome to Mumbai Munchies!")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Sell Snack")
        print("5. View All Snacks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                snack_name, price, availability = get_snack_details()
                snack_id = len(snack_inventory) + 1  # Generate a unique ID
                new_snack = Snack(snack_id, snack_name, price, availability)
                add_snack(new_snack)
                print("Snack added successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric values for price.")
            
        elif choice == "2":
            try:
                snack_id_to_remove = int(input("Enter snack ID to remove: "))
                remove_snack(snack_id_to_remove)
                print("Snack removed successfully!")
            except ValueError:
                print("Invalid input. Please enter a numeric snack ID.")
            
        elif choice == "3":
            try:
                snack_id_to_update = int(input("Enter snack ID to update: "))
                new_availability = input("Is the snack available (yes/no): ").lower() == "yes"
                update_snack_availability(snack_id_to_update, new_availability)
                print("Snack availability updated successfully!")
            except ValueError:
                print("Invalid input. Please enter a numeric snack ID.")
            
        elif choice == "4":
            try:
                snack_id_to_sell = int(input("Enter snack ID to sell: "))
                record_sale(snack_id_to_sell)
            except ValueError:
                print("Invalid input. Please enter a numeric snack ID.")
            
        elif choice == "5":
            for snack in snack_inventory:
                print("------------------------------")
                print("snackID:",snack["snack_id"])
                print("Name:",snack["name"])
                print("Price:",snack["price"])
                if snack["availability"]:
                    print("Available")
                else:
                    print("Not Available")
                print("------------------------------")


        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
