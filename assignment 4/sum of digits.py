def single_digit_sum(n, number):
    if len(str(number)) == n:
        total = sum(int(digit) for digit in str(number))
        while total >= 10:
            total = sum(int(digit) for digit in str(total))
        print(f"Sum of {n} digit number: {total}")
    else:
        print("Invalid input. The number does not match the given N.")

# Test Cases
tests = [(3, 143), (2, 158), (3, 14), (4, 148), (1, 4), (4, 7263)]
for n, number in tests:
    print(f"\nN = {n}, Number = {number}")
    single_digit_sum(n, number)
