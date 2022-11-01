# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# 5.07%,55.85%
class Solution(object):
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        
        pair = []
        dic = {'{':'}','(':')','[':']'}
        
        
        for i in s:
            if i in dic.keys():
                pair = [dic[i]] + pair
            else:
                if pair and i == pair[0]:
                    pair = pair[1:]
                else:
                    return False
        if pair == []:
            return True

# similar solution with append, pop
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {')':'(', '}':'{', ']':'['}

        for p in s:
            if p in lookup.values():
                stack.append(p)
            elif stack and lookup[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []

#