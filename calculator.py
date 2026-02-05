
print("\n============= CALCULATOR =============\n")

# ------- INPUT ----------

while True:
    try:
        num1 = float(input("Enter a first number: "))
        break
    except ValueError:
        print("We calculate with numbers only!\n")

while True:
    try:
        num2 = float(input("Enter a second number: "))
        break
    except ValueError:
        print("We calculate with numbers only!\n")

op_list = ["+","-","*","/"]
while True:
    operator = input("\nSelect the operation ( +, -, *, /): ")
    if operator in op_list:
        break
    print("We only provide these operations: ( +, -, *, /)")


# ------- CALCULATE --------

def calculate(num1, num2, operator):
    if operator == "+":
        print(f"\nThe addition of {num1} and {num2} is ", num1 + num2)
    elif operator == "-":
        print(f"\nThe subtraction of {num1} and {num2} is ", num1 - num2)
    elif operator == "*":
        print(f"\nThe multiplication of {num1} and {num2} is ", num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print(f"\n The {num1} cannot divide by zero")
        else:
            print(f"\nThe division of {num1} and {num2} is ", num1 / num2)
    else:
        print("\nOperation cannot be done.")

# ------ MAIN -------

def main():
    calculate(num1, num2, operator)

if __name__ == "__main__":
    main()
