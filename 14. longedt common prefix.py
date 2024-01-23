# 14. Longest common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        # first sorting the strs, and finding the minimum word length and finally comparing the longest same prefix
        else:
            strs.sort()
            first_word_length = len(strs[0])
            for i in range(1, len(strs)):
                length = min(first_word_length, len(strs[i]))
                while length > 0 and strs[0][0:length] != strs[i][0:length]:
                    length-=1
                    if length == 0:
                        return ""
            return strs[0][0:length]