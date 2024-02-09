class Solution(object):
    def removeDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 1):
                print(nums)
                if nums[i] == nums[j]:
                    nums.remove(nums[j])
                    
        return len(nums)


obj = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(obj.removeDuplicate(nums))
