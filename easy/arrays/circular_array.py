class Solution(object):
    def circular_sum_array(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Given an array of integers a. The task is to return
        another array b where b[i] = a[i  - 1] + a[i] + a[i + 1)

        example array a:
        [1,2,3,4,5]
        
        we want to create a new array 'b' based on the first array 'a'
        that holds the sum of the corresponding 3 elements denoted as:
        
        a[i]+a[i + 1]       +      a[i - 1] = 8
        [1,     2,     3,     4,     5]
        
        """
        n = len(nums)
        b = [0] * n
        
        for i in range(n):
            
            b[i] = nums[i - 1] + nums[i] + nums[(i + 1) % n]
        
        return b
    
obj = Solution()

newList = [1,2,3,4,7]

print(obj.circular_sum_array(newList))
