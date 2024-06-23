def length_of_longest_substring(s):
    hashmap = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in hashmap and hashmap[char] >= left:
            left = hashmap[char] + 1
        hashmap[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3
