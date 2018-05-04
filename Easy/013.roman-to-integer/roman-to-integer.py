class Solution:
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }
        ans = 0
        isTwo = 0
        for i,romanNumeral in enumerate(s):
            if((i+1 )< len(s)):
                if((s[i]+s[i+1]) in d):
                    ans += d[s[i]+s[i+1]] 
                    isTwo = 1
                    continue
            if (s[i] in d) and isTwo == 0:
                ans += d[s[i]]
            else:
                isTwo = 0
      
        return ans
    
      def romanToInt2(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V": 5, "X":10,"L":50,"C":100, "D":500, "M":1000}
        ans = 0
        for i in xrange(0, len(s) - 1):
            c = s[i]
            cafter = s[i + 1]
            if d[c] < d[cafter]:
                ans -= d[c]
            else:
                ans += d[c]
        ans += d[s[-1]]
        return ans