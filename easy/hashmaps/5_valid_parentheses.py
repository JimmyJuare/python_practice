class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        para_map = {
             '{':'}', 
             '[':']', 
             '(':')'
        }
        new_stack = []
        
        for i in s:
            
            if i in para_map:
                new_stack.append(i)
            else:
                if len(new_stack) == 0 or para_map[new_stack.pop()] != i:
                    return False
            
            print(new_stack)
        return len(new_stack) == 0
obj = Solution()
print(obj.isValid('()'))
