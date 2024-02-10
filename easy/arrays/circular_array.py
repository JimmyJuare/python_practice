class Solution(object):
    def circular_sum_array(self, nums):
        """
        we need to make each element of the second list equal to the corresponding element(list_a[i]) 
        plus the adjacent elements on both sides:

        left side: a[i - 1]
        right side: a[(i + 1) % n]

        example:

        we want to iterate over this list and add the sum of the current element to its adjacent 
        elements

        we want to prevent out of range indexing, in order to prevent out of range indexing, we will use
        modulo to return the remainder which we will use as an index

        list_a = [1,2,3,4]

        list_a[3] + list_a[3 - 1] + list_a[(3 + 1) % n] = list_a[0]

           4      +      3        + list_a[4 % 4] = list_a[0]
                                             | 
                                      list_a[0]
                               
        right side: a[(3 + 1) % n]

        
        """
        n = len(nums)
        b = [0] * n
        #[0,0,0,0,0]
        
        for i in range(n):
            
            b[i] = nums[i - 1] + nums[i] + nums[(i + 1) % n]

             
        return b
    
obj = Solution()

newList = [1,2,3,4,7]

print(obj.circular_sum_array(newList))
