def count_odd_even(m, n):
    odds = len([x for x in range(m, n + 1) if x % 2 != 0])
    evens = len([x for x in range(m, n + 1) if x % 2 == 0])
    
    print(f"Number of Odd Numbers = {odds}")
    print(f"Number of Even Numbers = {evens}")

# Test Cases
ranges = [(60, 300), (100, 100), (500, 100), (-5, 4), (12, -12)]
for m, n in ranges:
    print(f"\nM = {m}, N = {n}")
    count_odd_even(m, n)
