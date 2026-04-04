
# Iceage Hotel

# System-Time based on serving meal (Breakfast/Lunch/Snacks/Dinner)
# Take order, Ask any extra need
# Generate bill

from datetime import datetime

def get_food():
    current_hour = datetime.now().hour

    if 6 <= current_hour < 11:
        return "Breakfast"
    elif 12 <= current_hour < 15:
        return "Lunch"
    elif 16 <= current_hour < 18:
        return "Snacks"
    elif 20 <= current_hour < 24:
        return "Dinner"
    else:
        return "Closed"
    
def show_menu(food):
    menus = {
        "Breakfast": {"Idli": 20, "Dosa": 30, "Pongal": 50, "Coffee": 10},
        "Lunch": {"Meals": 50, "Briyani": 150},
        "Snacks": {"Samosa": 5, "Vada": 5, "Bajji": 5,"Tea": 10,"Coffee": 10},
        "Dinner": {"Chapati": 40, "Rice": 30}
    }

    if food in menus:
        print(f"\n {food.capitalize()} Menu:")
        for item, price in menus[food].items():
            print(f"{item} - ₹{price}")
        return menus[food]
    else:
        print("\nHotel is currently closed.")
        return None

def take_order(menu):
    order = {}
    
    while True:
        item = input("\n Enter item name (or type 'done'): ").title()
        
        if item.lower() == "done":
            break
        
        if item in menu:
            qty = int(input("Enter quantity: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not in menu!")

    return order

def ask_extra(order, menu):
    extra = input("\nDo you need anything extra? (yes/no): ").lower()
    
    if extra == "yes":
        print("\nYou can order more items:")
        return take_order(menu)
    
    return {}

def generate_bill(order, menu):
    total = 0
    
    print("\n BILL")
    print("----------------------")
    
    for item, qty in order.items():
        price = menu[item]
        cost = price * qty
        total += cost
        print(f"{item} x{qty} = ₹{cost}")
    
    print("----------------------")
    print(f"Total = ₹{total}")
    print("Thank you! Visit again...")


print("********** ICEAGE HOTEL **********")

food = get_food()
print(f"\nCurrent Meal Time: {food}")

menu = show_menu(food)

if menu:
    order = take_order(menu)
    extra_order = ask_extra(order, menu)
    for item, qty in extra_order.items():
        order[item] = order.get(item, 0) + qty
    generate_bill(order, menu)