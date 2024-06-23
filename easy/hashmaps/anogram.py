from collections import defaultdict

def group_anagrams(strs):
    hashmap = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        hashmap[key].append(s)
    return list(hashmap.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

