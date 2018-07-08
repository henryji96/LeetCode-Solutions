class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        uniqueCountIndex = {0: 0}
        maxLen = 0

        for index, num in enumerate(nums, 1):

            if num == 1:
                count += 1
            elif num == 0:
                count -= 1

            if count in uniqueCountIndex.keys():
                maxLen = max(maxLen, index - uniqueCountIndex[count])
            else:
                uniqueCountIndex[count] = index
        return maxLen
