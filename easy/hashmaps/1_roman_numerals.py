class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = list(s)
        romanNums = dict(
            {
                'I':1, 'V':5, 
                'X':10, 'L':50,
                'C':100, 'D':500,
                'M':1000
            })
        res = 0
        for i in range(len(nums)):
            
            if i > 0 and romanNums[nums[i]] > romanNums[nums[i - 1]]:
                res +=  romanNums[nums[i]] - 2 * romanNums[nums[i - 1]]
            else:
                res += romanNums[nums[i]]
            
        return res

obj = Solution()
print(obj.romanToInt('IV'))
