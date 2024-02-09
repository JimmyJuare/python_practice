"""

lets create a function that takes in a list (list_a) of numbers and iterates over that list
and checks if the current element (y = list_a[i + 1]) is either greater than both left(x = list_a[i]) 
and right(z = a[i + 2]) adjacent elements, and if so then we want to add (1) to the a newly 
created list (list_b)
----------------------------------------------------------------------------------------
Example input: [1, 2, 1, 0] 

2 is greater than both(1 > 2 < 1) 

it can also be denoted as (x > y < z) where (x = 1), (y = 2), and z = 1

therfore list_b = [1, 0]
                  /    \                    
        (1 > 2 < 1)  (2 < 1 < 0)
----------------------------------------------------------------------------------------

or if the current element (list_a[i + 1]) is less than both left (list_a[i]) and 
right (list_a[i + 2]) adjacent elements, we will also add (1) to list_b just like we did
when the current element was greater than both adjacent elements as shown above

----------------------------------------------------------------------------------------
Example input: [2, 1, 3, 4] 

1 is less than 2 and 3 (2 < 1 > 3)

being that 2 is on the left side and 3 is on the right side of
our current element being checked

making list_b = [1, 0]
                /    \                    
        (2 < 1 > 3)  (1 > 3 > 4)
----------------------------------------------------------------------------------------

otherwise append 0 to the corresponding elements for list_b

"""
