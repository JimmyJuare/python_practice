def second_largest(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second and number != first:
            second = number
    return second

# Test the function
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(second_largest([5, 5, 5, 5, 5]))      # Output: -inf (or a specific message if there is no second largest)
