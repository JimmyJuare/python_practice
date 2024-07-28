from collections import defaultdict, deque

def find_ladders(begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:
    if end_word not in word_list:
        return []

    word_list = set(word_list)
    result = []
    layer = {}
    layer[begin_word] = [[begin_word]]

    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == end_word:
                result.extend(k for k in layer[word])
            else:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_list:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]
        
        word_list -= set(new_layer.keys())
        layer = new_layer

    return result

# Example Usage
print(find_ladders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
