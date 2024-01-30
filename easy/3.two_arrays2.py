def two_array2(list_one, list_two):
    hash_map = {}
    for i in list_one:
        hash_map[i] = True
            
    for j in list_two:
        if j in hash_map:
            return True
    return False

list_one = ['a', 'b', 'c', 'd']
list_two = ['a', 'e', 'z', 'v']

print(two_array2(list_one, list_two))
