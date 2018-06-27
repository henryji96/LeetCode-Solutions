#hash table
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None

        for key,val in  Counter(nums).items():
            if val == 1:
                return key

#set
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None

        numSet = set()

        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        return numSet.pop()
