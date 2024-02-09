# 202. Happy number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            s=0
            while n>0:
                a = n % 10
                s+=a**2
                n//=10
            n=s
        return n==1