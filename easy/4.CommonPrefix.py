class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        
        """
        # 1.we want a place to store the first two characters
        letters = []
        # 2. we want to iterate through the list elements
        for el in range(len(strs)):
            letters.extend([[strs[el][0], strs[el][1]]])
        
        # 3. we want to compare those strings to the element to its right
        print(letters)
obj = Solution()
newList = ['preorder', 'prefix', 'premature']

print(obj.longestCommonPrefix(newList))
