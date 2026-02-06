
print("\n============= STATIONARY STORE ==============")

items = {
    "pen": 5,
    "pencil": 5,
    "eraser": 2,
    "sharpener": 3, 
    "scale": 10, 
    "note": 25,
    "paper": 1
}

def shop():
    total = 0
    while True:
        item = input("\nWhat do you want to buy?: ").lower()

        if item in items:
            quantity = int(input("How much quantity you need?: "))
            cost = items[item] * quantity
            total += cost
            print(f"Added {quantity} {item}(s) — ${cost:.2f}")

            more = input("\nDo you need anything else? (yes/no): ").lower()
            if more != "yes":
                print(f"\nItems purchased for ${total:.2f} 💵")
                print("Thank you for shopping!\n")
                break
        else:
            print("The item you want to buy is unavailable!\n")

def main():
    shop()

if __name__ == "__main__":
    main()