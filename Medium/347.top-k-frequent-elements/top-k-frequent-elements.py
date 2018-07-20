from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        return [item[0] for item in Counter(nums).most_common(k)]



from collections import Counter,defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):

        if len(nums) < k:
            return []

        freq = Counter(nums)
        bucket = defaultdict(list)

        for key in freq:
            f = freq[key]
            bucket[f].append(key)

        i = len(nums)
        ans = []
        while len(ans) < k:
            if bucket[i]:
                ans += bucket[i]
            i -= 1
        return ans
