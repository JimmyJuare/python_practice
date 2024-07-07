def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Test
print(flatten_list([[1, 2, [3]], 4]))  # Output: [1, 2, 3, 4]
