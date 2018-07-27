from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = Counter(nums)

        ans = 0
        for x in cnt:
            if x+1 in cnt:
                ans = max(ans, cnt[x] + cnt[x+1])
        return ans
