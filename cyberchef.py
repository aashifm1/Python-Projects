import base64

# Base conversion
BASE_MAP = {
    "bin": 2,
    "oct": 8,
    "dec": 10,
    "hex": 16
}

# Converts a number from any given base into decimal (base 10).
def to_decimal(value: str, base: int) -> int:
    return int(value, base)

# Converts a decimal number into binary, octal, hexadecimal.
def from_decimal(value: int, base: int) -> str:
    if base == 2:
        return bin(value)[2:]
    elif base == 8:
        return oct(value)[2:]
    elif base == 16:
        return hex(value)[2:]
    elif base == 10:
        return str(value)
    else:
        raise ValueError("Unsupported base found...")

def convert_number(value: str, from_base: int, to_base: int) -> str:
    decimal_value = to_decimal(value, from_base)
    return from_decimal(decimal_value, to_base)

# Base64 Conversion
def encode_base64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def decode_base64(text: str) -> str:
    return base64.b64decode(text.encode()).decode()

# Processing part
def process_operation(data: str, mode: str, data_type: str):

    # Number system operations
    if data_type in BASE_MAP:
        base = BASE_MAP[data_type]

        if mode == "encode":
            # decimal → selected base
            return from_decimal(int(data), base)

        elif mode == "decode":
            # selected base → decimal
            return str(int(data, base))

    # Base64 operations
    elif data_type == "base64":
        if mode == "encode":
            return encode_base64(data)
        elif mode == "decode":
            return decode_base64(data)

    else:
        raise ValueError("Unsupported data type")


def apply_chained_operations(data: str):
    current_data = data

    while True:
        print("\nChoose operation:")
        print("1. Encode")
        print("2. Decode")
        print("3. Stop chaining")

        choice = input("Select: ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid choice")
            continue

        mode = "encode" if choice == "1" else "decode"

        print("Available types: bin | oct | dec | hex | base64")
        data_type = input("Type: ").strip().lower()

        try:
            current_data = process_operation(current_data, mode, data_type)
            print("Result:", current_data)
        except Exception as e:
            print("Error:", e)

    return current_data


def main():
    print("=== Mini CyberChef ===")

    while True:
        print("\nMain Menu")
        print("1. Start Processing")
        print("2. Exit")

        choice = input("Select: ").strip()

        if choice == "2":
            print("Good bye...")
            break

        if choice == "1":
            user_input = input("Enter initial value: ").strip()

            try:
                final_result = apply_chained_operations(user_input)
                print("\nFinal Output:", final_result)
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    main()
