class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digitsStr = ""
        for digit in digits:
            digitsStr = digitsStr + str(digit)
        digitsInt = int(digitsStr) + 1
        ans = []
        for newDigit in str(digitsInt):
            ans.append(int(newDigit))
        return ans