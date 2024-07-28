def longest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s
    
    start, max_length = 0, 1

    for i in range(1, len(s)):
        even_palindrome = s[i-max_length:i+1]
        odd_palindrome = s[i-max_length-1:i+1]

        if i - max_length >= 0 and even_palindrome == even_palindrome[::-1]:
            start = i - max_length
            max_length += 1
        elif i - max_length - 1 >= 0 and odd_palindrome == odd_palindrome[::-1]:
      
