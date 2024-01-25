class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = list(s)
        for i in range(len(nums)):
            print(nums[i])
        
        print(nums)
        print('length', int(len(nums) - 1))
        
        romanNums = dict({1:'I'})
        if int(s) in romanNums:
            return True
        else:
            return False

obj = Solution()
print(obj.romanToInt('1454'))
