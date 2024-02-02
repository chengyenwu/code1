# 70. Climbing stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial
        twosteps = n//2
        k=0
        for i in range(twosteps+1):
            j = n-2*i
            m = factorial(i+j)//factorial(i)//factorial(j)
            k+=m
        return k
    
        # Solution 2. dynamic programming
        # if n == 1:
        #     print(1)

        # if n == 2:
        #     print(2)

        # dp = [0] * (n + 1)
        # print(M)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]