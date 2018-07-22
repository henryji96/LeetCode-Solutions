class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        xStr = "".join(str(x) for x in digits)
        plus1 = int(xStr) + 1

        return [int(x) for x in str(plus1)]
