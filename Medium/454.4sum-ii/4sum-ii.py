from collections import defaultdict
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        m = defaultdict(int)

        for a in A:
            for b in B:
                m[a + b] += 1

        ans = 0
        for c in C:
            for d in D:
                if -c-d in m:
                    ans += m[-c-d]
        return ans
