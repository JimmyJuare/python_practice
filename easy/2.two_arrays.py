list_one = ['a', 'b', 'c', 'd']
list_two = ['a', 'e', 'z', 'v']
list_three = ['a', 'b', 'z', 'v']
list_four = ['q', 'e', 'u', 'i']

'''

find the common
element between two arrays
'''
def common_data(list_one, list_two):
    for i in list_one:
        if i in list_two:
            return True
    return False

print(common_data(list_three, list_four))
