# ------------------------------
# Restaurant Menu with Order System
# ------------------------------

menu = {
    "India Bina Vadapav": {
        "Classic Vada Pav": 35,
        "Cheese Vada Pav": 55,
        "Butter Vada Pav": 45,
        "Butter Cheese Vada Pav": 65,
        "Cheese Burst Vada Pav": 75,
        "Paneer Vada Pav": 75,
        "Paneer Cheese Vada Pav": 95,
        "Paneer Butter Vada Pav": 85,
        "Paneer Butter Cheese Vada Pav": 105,
        "Peri Peri Vada Pav": 45,
        "Peri Peri Cheese Vada Pav": 65,
        "Peri Peri Paneer Vada Pav": 85,
        "Peri Peri Paneer Cheese Vada Pav": 105
    },

    "India Bina Samose": {
        "Classic Samosa Pav": 35,
        "Cheese Samosa Pav": 55,
        "Butter Samosa Pav": 45,
        "Butter Cheese Samosa Pav": 65,
        "Paneer Samosa Pav": 75,
        "Paneer Cheese Samosa Pav": 95,
        "Paneer Butter Samosa Pav": 85,
        "Paneer Butter Cheese Samosa Pav": 105,
        "Peri Peri Samosa Pav": 45,
        "Peri Peri Cheese Samosa Pav": 65,
        "Peri Peri Paneer Samosa Pav": 85,
        "Peri Peri Paneer Cheese Samosa Pav": 105
    },

    "Barso Garam Pee Uthyo": {
        "Tea": 15,
        "Coffee": 20
    },

    "Bite Bina Pav Uthyo": {
        "Veg Puff": 25,
        "Cheese Puff": 40,
        "Paneer Puff": 50,
        "Paneer Cheese Puff": 65,
        "Peri Peri Puff": 35,
        "Peri Peri Cheese Puff": 50,
        "Peri Peri Paneer Puff": 55,
        "Peri Peri Paneer Cheese Puff": 75
    },

    "Ek Dumdaar": {
        "Schezwan Uthyo": 40,
        "Cheese Schezwan Uthyo": 60,
        "Paneer Schezwan Uthyo": 80,
        "Paneer Cheese Schezwan Uthyo": 100
    },

    "Pote Ne Bhog": {
        "Maggi Plain": 40,
        "Cheese Maggi": 60,
        "Paneer Maggi": 80,
        "Paneer Cheese Maggi": 100,
        "Peri Peri Maggi": 50,
        "Peri Peri Cheese Maggi": 70,
        "Peri Peri Paneer Maggi": 90,
        "Peri Peri Paneer Cheese Maggi": 110,
        "Mast Special Pulav": 120
    },

    "Tandoori Videsi Pav": {
        "Tandoori Cheese Pav": 70,
        "Paneer Tandoori Pav": 90,
        "Paneer Cheese Tandoori Pav": 110,
        "Butter Tandoori Cheese Pav": 80,
        "Butter Paneer Tandoori Pav": 100,
        "Butter Paneer Cheese Tandoori Pav": 120
    },

    "And Yu And Mast Wada": {
        "Egg Puff": 40,
        "Cheese Egg Puff": 55,
        "Butter Egg Puff": 50,
        "Butter Cheese Egg Puff": 65,
        "Peri Peri Egg Puff": 50,
        "Peri Peri Cheese Egg Puff": 65,
        "Paneer Egg Puff": 70,
        "Paneer Cheese Egg Puff": 90
    },

    "Platter Donish Bantai": {
        "Vada Pav Platter": 160,
        "Samosa Pav Platter": 160,
        "Mix Platter (Vada Pav + Samosa Pav)": 180,
        "Paneer Vada Pav Platter": 200,
        "Paneer Samosa Pav Platter": 200,
        "Paneer Mix Platter": 220
    },

    "Bhashi Videsi Pav Uthyo": {
        "Cheese Burger": 90,
        "Paneer Burger": 110,
        "Paneer Cheese Burger": 130,
        "French Fries": 60,
        "Cheese French Fries": 80,
        "Peri Peri French Fries": 70
    },

    "Mara Yar Tari Dishum": {
        "Pav Bhaji": 90,
        "Cheese Pav Bhaji": 110,
        "Paneer Pav Bhaji": 120,
        "Paneer Cheese Pav Bhaji": 140,
        "Butter Pav Bhaji": 100,
        "Butter Cheese Pav Bhaji": 120
    },

    "Bite Bar Baar Khayo": {
        "Bhel Puri": 50,
        "Cheese Bhel": 70,
        "Sev Puri": 50,
        "Cheese Sev Puri": 70,
        "Masala Puri": 50,
        "Cheese Masala Puri": 70
    },

    "Kacchi Noodles": {
        "Veg Hakka Noodles": 100,
        "Veg Schezwan Noodles": 110,
        "Paneer Noodles": 120,
        "Paneer Schezwan Noodles": 130
    }
}


# ------------------------------
# Order Taking System
# ------------------------------
def show_menu():
    print("\n========== MENU ==========")
    for category, items in menu.items():
        print(f"\n--- {category} ---")
        for item, price in items.items():
            print(f"{item} - ₹{price}")
    print("==========================")

def take_order():
    bill = {}
    while True:
        item = input("\nEnter item name to order (or 'done' to finish): ").strip()
        if item.lower() == "done":
            break
        
        # Search item in menu
        found = False
        for category in menu:
            if item in menu[category]:
                qty = int(input("Enter quantity: "))
                bill[item] = bill.get(item, 0) + qty * menu[category][item]
                print(f"✅ Added {qty} x {item}")
                found = True
                break
        if not found:
            print("❌ Item not found in menu! Try again.")
    
    return bill

def print_bill(bill):
    print("\n========== BILL ==========")
    total = 0
    for item, price in bill.items():
        print(f"{item} - ₹{price}")
        total += price
    print("--------------------------")
    print(f"TOTAL: ₹{total}")
    print("==========================")

# ------------------------------
# Main Program
# ------------------------------
show_menu()
order = take_order()
print_bill(order)

