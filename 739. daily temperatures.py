# 739. Daily temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dynamic programming + stack (running time: O(n))
        dp=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                dp[prev_index] = i-prev_index
            stack.append(i)
        return dp