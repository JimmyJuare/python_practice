"""
        :type strs: List[str]
        :rtype: str
        
        Can Include
        Tasks that require a combination of 3 to 5 basic concepts. For example:
        Splitting a string into substrings, modifying each substring and comparing
        with other strings.
        Iterating over an array to produce two new arrays given some conditions, modifying 
        the second array and appending it to the beginning of the first array.
        Should usually be solvable using one to two nested loops.
        The task description should clearly state the implementation steps.

        x Should Exclude
        Anything that requires noticing or proving a certain pattern.
        Anything that requires optimizing an algorithm.
        Anything that requires a knowledge of classic algo-rithms.
        Example:
        Given a list of words (consisting of lowercase English letters) and a complex
        word written in camelCase (con-sisting of English letters), check if the complex
        word consists of words from the given list.
"""
class Solution(object):
    def _helper(self, word):
      words_in_camel_case = []
      current_word = ""

      for char in word:
        if char.isupper():
          if current_word:
            words_in_camel_case.append(current_word)
            current_word = char.lower()
            print(current_word)
            print(words_in_camel_case)
          else:
            current_word += char.lower()
            print(words_in_camel_case)
        else:
          current_word += char
          print(current_word)
          print(words_in_camel_case)
      
      if current_word:
        words_in_camel_case.append(current_word)
        print(words_in_camel_case)
      
      return words_in_camel_case
            
    def CamelCase(self, camelCase, strs):
        # for i in range(len(strs)):
        #   self._helper(strs[i])
        lowercase_list = [string.lower() for string in strs]
        words = self._helper(camelCase)
        # print(words)
        for word in words:
          if word not in lowercase_list:
            return False
        return True

obj = Solution()
print(obj.CamelCase('jimmyMac' , ['jimmy', 'Billy', 'Mac']))
