# 58. Length of last world
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = len(s)-1
        ans = 0
        while s[index] == " ":
            index-=1
        while index >= 0 and s[index] != " ":
            ans+=1
            index-=1
        return ans