# 125. Valid palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == " ":
            return True
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i
        if new_s.lower() == new_s.lower()[::-1]:
            return True
        else:
            return False
        
        # s=s.lower()
        # p=0
        # q=len(s)-1
        # while p<q:
        #     while p<q and not s[p].isalnum():
        #         p=p+1
                    
        #     while q>p and not s[q].isalnum():
        #         q=q-1
                    
        #     if s[p].isalnum() and s[q].isalnum():
        #         if s[p]==s[q]:
        #             p=p+1
        #             q=q-1
        #         else:
        #             return False   
        # return True