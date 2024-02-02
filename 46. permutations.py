# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    # Solution 1. 不要用index解，直接搜尋哪個元素
        def dfs(cur):  
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for n in nums:
                if n not in cur:
                    cur.append(n)
                    dfs(cur)
                    cur.pop()
        res = []
        dfs([])
        return res
        
    # Solution 2. 用index解
        length = len(nums)
        def dfs(nums, curr = None):
            if curr == None:
                curr = []
            if len(curr) == length:
                ans.append(curr.copy())
            for index in range(len(nums)):
                curr.append(nums[index])
                dfs(nums[:index]+nums[index+1:], curr)
                curr.pop()
        
        ans=[]
        dfs(nums)
        return ans