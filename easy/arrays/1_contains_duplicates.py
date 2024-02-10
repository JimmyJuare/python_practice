class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort()
        
        print(nums)
        for i in range(len(nums) - 1):
            
            if nums[i] == nums[i + 1]:
                return True

        return False


obj = Solution()
newList = [22, 14, 18, 2, 22]
print(obj.containsDuplicate(newList))
