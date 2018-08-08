class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        numsSet = set(nums)
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in numsSet:
                ans.append(i)
        return ans


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []


        return list( set([i for i in range(1, len(nums) + 1)]) - set(nums) )
        
