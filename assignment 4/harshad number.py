def is_harshad_number(number):
    if isinstance(number, int) and number > 0:
        digit_sum = sum(int(digit) for digit in str(number))
        if number % digit_sum == 0:
            print(f"Given number is Harshad number")
        else:
            print(f"Given number is not a Harshad number")
    else:
        print("Invalid input. Please enter a positive integer.")

# Test Cases
numbers = [21, 6804, 378, 111, 0, 145.678]
for number in numbers:
    print(f"\nEnter the number: {number}")
    is_harshad_number(number)
