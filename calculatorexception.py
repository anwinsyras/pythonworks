try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\n1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        print("Result:", a / b)

    else:
        print("Invalid choice")

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")