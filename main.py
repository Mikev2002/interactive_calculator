# main.py

from calculator import operations

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the CLI Calculator!")
    print("Available operations: add, subtract, multiply, divide, quit")

    while True:
        op = input("\nChoose operation: ").lower()

        if op == "quit":
            print("Goodbye!")
            break

        if op not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if op == "add":
                result = operations.add(a, b)
            elif op == "subtract":
                result = operations.subtract(a, b)
            elif op == "multiply":
                result = operations.multiply(a, b)
            elif op == "divide":
                result = operations.divide(a, b)

            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
