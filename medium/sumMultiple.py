def sum_multiples(n, multiples):
    total_sum = 0
    for i in range(1, n):
        if any(i % x == 0 for x in multiples):
            total_sum += i
    return total_sum

# Test
print(sum_multiples(20, [3, 5]))  # Output: 78
