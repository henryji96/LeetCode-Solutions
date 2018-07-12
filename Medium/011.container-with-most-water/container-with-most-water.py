class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l = 0
        r = len(height) - 1

        while  l < r:
            area = self.computeArea(height[l],l,height[r],r)
            ans = max(ans, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans

    def computeArea(self, h1, i1, h2, i2):
        return min(h1, h2)* (i2 - i1)
