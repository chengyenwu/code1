# 62. Unique paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Using factorial method
        def factorial(k):
            result = 1
            for i in range(1, k+1):
                result = result * i
            return result
        return (factorial(m-1+n-1)//factorial(m-1)//factorial(n-1))