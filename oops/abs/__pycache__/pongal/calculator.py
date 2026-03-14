while True:
    print("\nScientific Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    elif choice == 5:
        a = int(input("Enter base: "))
        b = int(input("Enter power: "))
        result = 1
        for i in range(b):
            result = result * a
        print("Result:", result)

    elif choice == 6:
        n = float(input("Enter number: "))
        print("Result:", n ** 0.5)

    elif choice == 7:
        n = int(input("Enter number: "))
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print("Result:", fact)

    elif choice == 8:
        print("Calculator closed")
        break

    else:
        print("Invalid choice")