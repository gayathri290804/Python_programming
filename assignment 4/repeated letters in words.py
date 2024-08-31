from collections import Counter

def count_repeated_letters(word):
    counter = Counter(word)
    repeated = sum(1 for count in counter.values() if count > 1)
    print(f"Number of repeated letters = {repeated}")

# Test Cases
words = ["TEMPLE", "HYPOTHECATION", "MATRICULATION", "MANIPULATION"]
for word in words:
    print(f"\nWord: {word}")
    count_repeated_letters(word)
