class Solution(object):
    def CamelCase(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        Can Include
        • Implementing a specific comparator for strings.
        • Implementing a specific merge function for arrays.
        • Other implementation challenges that clearly explain
          what needs to be done and require translating the
          instructions into code
         
        Should Exclude
        • Anything that requires noticing or proving a certain
        pattern.
        • Anything that requires optimizing an algorithm with what 
         advanced data structures like binary indexed trees,
         etc.
        • Anything from special topics like graphs, number theory, or dynamic programming.
        
        Given two strings, merge them with the following merge function:
        
        instead of comparing the characters in the usual lexicographical order, 
        compare them based on how many times they occur in their respective strings. 
        Fewer occurrences mean the character is considered smaller; in case of equality, 
        compare them lexicograph-ically; in case of equality, take the character from the 
        first string.
        """
        
