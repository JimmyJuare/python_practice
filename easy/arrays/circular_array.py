class Solution(object):
    def circular_sum_array(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        example array a:
        [1,2,3,4,5]
        
        we want to create a new array 'b' based on the first array 'a'
        that holds the sum of the corresponding 3 elements denoted as:
        
          a[i], a[i + 1]             a[i - 1]
        [   1,     2,     3,     4,     5]
        
        """
        n = len(nums)
        newList = [0] * n
        
        
