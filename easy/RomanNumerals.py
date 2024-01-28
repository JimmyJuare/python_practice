class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = list(s)
        romanNums = dict({'I':1, 'V':5, 'X':10})
        
        for i in range(len(nums)):
            print('nums', nums[i])
        
        print(nums)
        print('length', int(len(nums)))
        
        if int(s) in romanNums:
            return romanNums.get(int(s))
        else:
            return False

obj = Solution()
print(obj.romanToInt('1'))
