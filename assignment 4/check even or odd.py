def check_even_odd(number):
    if isinstance(number, int) or (isinstance(number, float) and number.is_integer()):
        if int(number) % 2 == 0:
            print(f"The given number is even")
        else:
            print(f"The given number is odd")
    else:
        print(f"Invalid input. Please enter an integer.")

# Test Cases
numbers = [6561, 0, -1254, "A144", 145.23, 23.456]
for number in numbers:
    print(f"\nEnter the number: {number}")
    check_even_odd(number)
