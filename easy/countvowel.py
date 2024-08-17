def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

# Example usage
print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1
