def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            
            choice = input("Enter the number of the operation (1/2/3/4) or 'q' to quit: ").strip()
            if choice.lower() == 'q':
                print("Exiting the calculator. Goodbye!")
                break
            
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please choose a valid operation.")
                continue
            
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

           
            if choice == '1':
                print(f"The result of {num1} + {num2} is {num1 + num2}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is {num1 - num2}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    print(f"The result of {num1} / {num2} is {num1 / num2}")

        except ValueError:
            print("Invalid input. Please enter numerical values.")
        print()  


if __name__ == "__main__":
    calculator()
