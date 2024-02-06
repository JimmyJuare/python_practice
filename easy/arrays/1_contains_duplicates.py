class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        j = 0
        for i in range(len(nums)):
            print(nums[i])
            for j in range(i + 1, len(nums)):
                print("j", nums[j])
                
                if nums[i] == nums[j]:
                    return True

        return False


obj = Solution()
newList = [2, 14, 18, 22, 22]
print(obj.containsDuplicate(newList))
