import re
from collections import defaultdict

def word_frequency(s):
    word_count = defaultdict(int)
    words = re.findall(r'\b\w+\b', s.lower())
    for word in words:
        word_count[word] += 1
    return dict(word_count)

# Test
print(word_frequency("Hello world! Hello, Python!"))  # Output: {'hello': 2, 'world': 1, 'python': 1}
