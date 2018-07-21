from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for s in strs:
            sortS = "".join(sorted(s))
            anagrams[sortS].append(s)

        return list(anagrams.values())

                
