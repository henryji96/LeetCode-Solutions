from collections import Counter
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []
        for num, cnt in Counter(nums).items():
            if cnt >= 2:
                ans.append(num)
        return ans



class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []
        for num in nums:
            idx = abs(num) - 1

            if nums[idx] >= 0:
                nums[idx] = -nums[idx]
            else:
                ans.append(idx + 1)
        return ans
