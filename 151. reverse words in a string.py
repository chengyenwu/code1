# 151. Reverse words in a string
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = " ".join(words[::-1])
        return reversed_words

        # wrong answer
        # temp = []
        # result = ""
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] != " ":
        #         temp.append(s[i])
        #     else:
        #         result += ''.join(temp[::-1]) + " "
        #         temp.clear()
        # result += ''.join(temp[::-1])
        # return result