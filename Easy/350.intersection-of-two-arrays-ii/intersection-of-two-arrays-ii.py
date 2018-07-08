class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            shortNums = nums1
            longNums = nums2
        else:
            shortNums = nums2
            longNums = nums1

        ans = []
        for num in shortNums:
            if num in longNums:
                ans.append(num)
                longNums.remove(num)

        return ans

from collections import Counter    
class Solution2:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            shortNums = nums1
            longNums = nums2
        else:
            shortNums = nums2
            longNums = nums1

        ans = []
        longCnt = Counter(longNums)
        for num in shortNums:
            if num in longCnt:
                longCnt[num] -= 1

                ans.append(num)
                if longCnt[num] == 0:
                    del longCnt[num]

        return ans
