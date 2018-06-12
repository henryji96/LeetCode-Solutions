class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        if target >= letters[-1]:
            return letters[0]

        low = 0
        high = len(letters)
        middle = low + (high - low) // 2
        while low <= high:
            if target >= letters[middle]:
                low = middle + 1
                middle = low + (high - low) // 2
            else:
                high = middle - 1
                middle = low + (high - low) // 2
        return letters[low]

if __name__ == '__main__':
    s = Solution()
    print(s.nextGreatestLetter(["c", "f", "j"],"j"))
