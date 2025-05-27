import math

def display_menu():
    print("\n=== CLI Calculator (Multi-Number / Expression) ===")
    print("1. Addition (e.g., 2+3+4)")
    print("2. Subtraction (e.g., 10-3-2)")
    print("3. Multiplication (e.g., 2*3*4)")
    print("4. Division (e.g., 100/5/2)")
    print("5. Modulus (e.g., 20%3)")
    print("6. Exponent (e.g., 2**3)")
    print("7. Square Root (enter comma-separated numbers)")
    print("8. Logarithm base 10 (enter comma-separated numbers)")
    print("9. Evaluate full expression (e.g., 2 + 3 * (4 - 1))")
    print("0. Exit")

def evaluate_expression(expr):
    try:
        result = eval(expr)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

def get_number_list(prompt):
    numbers = input(prompt)
    try:
        return list(map(float, numbers.split(',')))
    except ValueError:
        print("Invalid input. Please enter comma-separated numbers.")
        return []

def main():
    history = []

    while True:
        display_menu()
        choice = input("Select menu (0-9): ").strip()

        if choice in ["1", "2", "3", "4", "5", "6"]:
            expr = input("Enter expression (e.g., 2+3+4): ").strip()
            result = evaluate_expression(expr)

        elif choice == "7":
            nums = get_number_list("Enter numbers (comma-separated): ")
            for n in nums:
                if n < 0:
                    print(f"Square root of {n} is invalid.")
                else:
                    print(f"√{n} = {math.sqrt(n)}")

            result = None  

        elif choice == "8":
            nums = get_number_list("Enter numbers (comma-separated): ")
            for n in nums:
                if n <= 0:
                    print(f"log10({n}) is invalid.")
                else:
                    print(f"log10({n}) = {math.log10(n)}")

            result = None

        elif choice == "9":
            expr = input("Enter full expression: ")
            result = evaluate_expression(expr)

        elif choice == "0":
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        # Save history if there's a valid result
        if result is not None:
            history.append(str(result))

    # Display history
    if history:
        print("\n=== Calculation History ===")
        for i, h in enumerate(history, 1):
            print(f"{i}. {h}")

if __name__ == "__main__":
    main()
