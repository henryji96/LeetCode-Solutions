class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s


        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        sl = list(s)


        l = 0
        h = len(sl) - 1

        while l < h:
            if sl[l] not in vowels:
                l += 1
            if sl[h] not in vowels:
                h -= 1
            if sl[l] in vowels and sl[h] in vowels:
                temp = sl[l]
                sl[l] = sl[h]
                sl[h] = temp
                l += 1
                h -= 1

        return "".join(sl)
