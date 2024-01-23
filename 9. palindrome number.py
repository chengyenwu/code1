# 9. Palindrome number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # turing integer into string
        strx = str(x)
        stry = strx[::-1]
        if strx == stry:
            return True
        else:
            return False
        
        # solution 2.
        # original = x
        # revnum = 0
        # if x<0:
        #     return False
        # if x>0:
        #     while x>0:
        #         revnum = revnum * 10 + x % 10
        #         x = x // 10
        # if revnum == original:
        #     return True
        # else:
        #     return False