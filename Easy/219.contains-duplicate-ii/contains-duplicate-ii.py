from collections import defaultdict
import sys
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numsPos = defaultdict(list)

        for i, num in enumerate(nums):
            numsPos[num].append(i)

        for pos in numsPos.values():
            if len(pos) >= 2 and self.getMinDiff(pos) <= k:
                return True
        return False
                

    def getMinDiff(self, pos):
        ans = sys.maxsize
        for i in range(1, len(pos)):
            ans = min(ans, pos[i] - pos[i-1])
        return ans



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastPos = dict()

        for i, val in enumerate(nums):
            if val in lastPos and i - lastPos[val] <= k:
                return True

            lastPos[val] = i

        return False
