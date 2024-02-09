# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Solution 1. 不要用index解，直接搜尋哪個元素
        def dfs(curr, result):
            if len(curr) == len(nums):
                result.append(curr.copy())
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(curr, result)
                    curr.pop()
        result = []
        curr = []
        dfs(curr, result)
        return result
    # recording
    # n=1
    # cur = [1]
    # dfs([1])
    #     n=2
    #     cur = [1,2]
    #     dfs([1,2])
    #         n=3
    #         cur = [1,2,3]
    #         dfs([1,2,3]) => res = [[1,2,3]]
    #         cur = [1,2]
    #     cur = [1]
    #     n=3
    #     cur = [1,3]
    #     dfs([1,3])
    #         n=2
    #         cur = [1,3,2]
    #         dfs([1,3,2]) => res = [[1,2,3], [1,3,2]]
    #         cur = [1,3]
    #     cur = [1]
    # cur=[]
    # n=2
    # cur = [2]
    # dfs([2])
    #     n=1
    #     cur = [2,1]
    #     dfs([2,1])
    #         n=3
    #         cur = [2,1,3]
    #         dfs([2,1,3]) => res = [[1,2,3], [1,3,2], [2,1,3]]
    #         cur = [2,1]
    #     cur = [2]
    #     n=3
    #     cur = [2,3]
    #     dfs([2,3])
    #         n=1
    #         cur = [2,3,1]
    #         dfs([2,3,1]) => res = [[1,2,3], [1,3,2], [2,1,3], [2,3,1]]
    #         cur = [2,3]
    #     cur = [2]
    # cur=[]
    # n=3
    # cur = [3]
    # dfs([3])
    #     n=1
    #     cur = [3,1]
    #     dfs([3,1])
    #         n=2
    #         cur = [3,1,2]
    #         dfs([3,1,2]) => res = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2]]
    #         cur = [3,1]
    #     cur = [3]
    #     n=2
    #     cur = [3,2]
    #     dfs([3,2])
    #         n=1
    #         cur = [3,2,1]
    #         dfs([3,2,1]) => res = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    #         cur = [3,2]
    #     cur = [3]
    # cur=[]

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