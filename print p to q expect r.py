def print_without_digit(p, q, r):
    result = [x for x in range(p, q + 1) if str(r) not in str(x)]
    print(f"Numbers are = {', '.join(map(str, result))}")

# Test Cases
tests = [(60, 70, 3), (200, 200, 5), (100, 200, 0), (-100, 100, 5)]
for p, q, r in tests:
    print(f"\nP = {p}, Q = {q}, R = {r}")
    print_without_digit(p, q, r)
