# 13. Roman to integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build a dictionary
        dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        # compare index i number with index i+1 number 
        ans = 0
        for a in range(len(s)-1):
            if dic[s[a]] >= dic[s[a+1]]:
                ans = ans + dic[s[a]]
            if dic[s[a]] < dic[s[a+1]]:
                ans = ans - dic[s[a]]
        ans = ans + dic[s[-1]]
        return ans