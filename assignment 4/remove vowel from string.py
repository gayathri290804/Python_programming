def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    result = ''.join([ch for ch in string if ch not in vowels])
    print(f"The string without vowels is: {result}")

# Example
string = "we can play the game"
print(f"\nEnter a string: {string}")
remove_vowels(string)
