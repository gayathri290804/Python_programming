def odd_and_even_between(m, n):
    odds = [x for x in range(m, n+1) if x % 2 != 0]
    evens = [x for x in range(m, n+1) if x % 2 == 0]
    
    print(f"All Odd Numbers = {', '.join(map(str, odds))}")
    print(f"All Even Numbers = {', '.join(map(str, evens))}")

# Test Cases
ranges = [(6, 15), (100, 100), (500, 100), (-5, 4), (72, -72), (0, 0)]
for m, n in ranges:
    print(f"\nM = {m}, N = {n}")
    odd_and_even_between(m, n)
