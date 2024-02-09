# 326. Power of three
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n==1:
            return True
        while n%3==0:
            n/=3
        return n==1

        # if n <= 0:
        #     return False
        # while n>1:
        #     if n%3!=0:
        #         return False
        #     n=n/3
        # return True