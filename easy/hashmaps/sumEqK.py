def subarray_sum(nums, k):
    hashmap = {0: 1}
    count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum - k in hashmap:
            count += hashmap[current_sum - k]
        hashmap[current_sum] = hashmap.get(current_sum, 0) + 1
    return count

# Example usage
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output: 2
