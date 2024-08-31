def sort_vowels_consonants(word):
    vowels = sorted([ch for ch in word if ch in 'AEIOU'])
    consonants = sorted([ch for ch in word if ch not in 'AEIOU'])
    
    print(f"Vowels in alphabetical order: {', '.join(vowels)}")
    print(f"Consonants in alphabetical order: {', '.join(consonants)}")

# Test Cases
words = ["EDUCATION", "HYPOTHECATION", "MATRICULATION", "MANIPULATION", "SEDIMENTATION", "EXPERIMENTATION"]
for word in words:
    print(f"\nWord: {word}")
    sort_vowels_consonants(word)
