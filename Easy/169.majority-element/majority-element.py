from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]


if __name__ == '__main__':
    s = Solution()
    ans = s.majorityElement([2,2,1,1,1,2,2])
    print(ans)
