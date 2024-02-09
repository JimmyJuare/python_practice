class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


obj = Solution()
newList = [2, 14, 18, 22, 22]
print(obj.containsDuplicate(newList))
