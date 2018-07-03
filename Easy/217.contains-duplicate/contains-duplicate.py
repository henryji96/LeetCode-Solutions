from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = dict(Counter(nums))
        for v in numDict.values():
            if v > 1:
                return True
        return False

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
