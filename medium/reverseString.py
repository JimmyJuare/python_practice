def reverse_words(s):
    words = s.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Test
print(reverse_words("Hello world"))  # Output: 'world Hello'
