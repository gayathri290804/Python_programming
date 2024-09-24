def calculate_mean(n, case):
    if n <= 0:
        print("Invalid N value. N should be positive.")
        return

    if case == 1:  # Mean of first N odd numbers
        numbers = [x for x in range(1, 2 * n, 2)]
    elif case == 2:  # Mean of first N even numbers
        numbers = [x for x in range(2, 2 * n + 1, 2)]
    elif case == 3:  # Mean of first N square numbers
        numbers = [x ** 2 for x in range(1, n + 1)]
    elif case == 4:  # Mean of first N cube numbers
        numbers = [x ** 3 for x in range(1, n + 1)]
    else:
        print("Invalid case number.")
        return

    mean = sum(numbers) / len(numbers)
    print(f"Mean of first {n} {'odd' if case == 1 else 'even' if case == 2 else 'square' if case == 3 else 'cube'} numbers: {mean}")

# Test Cases
tests = [(5, 2), (16, 1), (-8, 2), (0, 3)]
for n, case in tests:
    print(f"\nN = {n}, Case = {case}")
    calculate_mean(n, case)
