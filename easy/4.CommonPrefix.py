class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Sort the list of strings lexicographically
        strs.sort()
        
        # Consider the first and last string after sorting
        
        res = ''
        i = 0
            
        while i < len(strs[0]) and i < len(strs[-1]) and strs[0][i] == strs[-1][i]:
           
            res += strs[0][i]
            
            i += 1

        return res

obj = Solution()
newList = ["flower","flower","flower","flower"]

print(obj.longestCommonPrefix(newList))
