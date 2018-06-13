class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numDict = {}
        for num in nums:
            if num not in numDict.keys():
                numDict[num] = 0
            numDict[num] += 1


        for key, value in numDict.items():
            if value > (len(nums) // 2):
                return key

if __name__ == '__main__':
    s = Solution()
    ans = s.majorityElement([2,2,1,1,1,2,2])
    print(ans)
