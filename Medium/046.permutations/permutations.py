class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []

        def dfs(nums, tempArr):

            if len(tempArr) == len(nums):
                self.ans.append(tempArr[:])
                return

            for num in nums:
                if num in tempArr:
                    continue
                tempArr.append(num)
                dfs(nums,  tempArr)
                tempArr.pop()

        dfs(nums, [])

        return self.ans




if __name__ == '__main__':
    s = Solution()
    ans = s.permute([1,2,3])
    print(ans)
