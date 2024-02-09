# 242. Valid anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1.
        if len(s) != len(t):
            return False

        s_count = defaultdict(int) 
        for char in s:
            s_count[char] += 1
            print(s_count)
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
            print(t_count)

        return s_count == t_count

        # sloution 2.
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        return ls == lt