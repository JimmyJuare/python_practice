def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[-1]

# Example Usage
print(word_break("leetcode", ["leet", "code"]))  # Output: True
print(word_break("applepenapple", ["apple", "pen"]))  # Output: True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
