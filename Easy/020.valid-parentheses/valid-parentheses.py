class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        validParentheses = ['()', '{}', '[]']
        
        stack = []
        for c in s:
            stack.append(c)
            if(len(stack) >= 2 and stack[-2]+stack[-1] in validParentheses):
                stack.pop()
                stack.pop()
        return len(stack) == 0