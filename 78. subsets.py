# 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, curr_index, path):
            result.append(path)
            for i in range(curr_index, len(nums)):
                dfs(nums, i+1, path+[nums[i]])
        
        result=[]
        path=[]
        dfs(nums, 0, path)
        return result
    
        # Recording
        nums=[1,2,3] , len(nums)=3
        dfs(nums, 0, [])
            result.append([])
            for i in range(0, 3):
                # i=0 
                print(0, result) => []
                dfs(nums, 1, []+[1]=[1])
                    result.append([1])
                    for i in range(1, 3):
                        # i=1
                        print(1, result) => [[], [1]] 
                        dfs(nums, 2, [1]+[2]=[1, 2])
                            result.append([1, 2])
                            for i in range(2, 3):
                            # i=2
                            print(2, result) => [[], [1], [1, 2]]
                            dfs(nums, 3, [1, 2]+[3]=[1, 2, 3])
                                result.append([1, 2, 3])
                                for i in range(3, 3): no for loop
                            print(result) => [[], [1], [1, 2], [1, 2, 3]]
                        print(result) => [[], [1], [1, 2], [1, 2, 3]]
                        # i=2
                        print(2, result) => [[], [1], [1, 2], [1, 2, 3]]
                        dfs(nums, 3, [1]+[3]=[1, 3])
                            result.append([1, 3])
                            for i in range(3, 3): no for loop
                        print(result) => [[], [1], [1, 2], [1, 2, 3], [1, 3]]
                print(result) => [[], [1], [1, 2], [1, 2, 3], [1, 3]]
                # i=1
                print(1, result) => [[], [1], [1, 2], [1, 2, 3], [1, 3]]
                dfs(nums, 2, []+[2]=[2])
                    result.append([2])
                for i in range(2, 3):
                    # i=2
                    print(2, result) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
                    dfs(nums, 3, [2]+[3]=[2, 3])
                        result.append([2, 3])
                        for i in range(3, 3): no for loop
                    print(result) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
                print(result) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
                # i=2
                print(2, result) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
                dfs(nums, 3, []+[3]=[3])
                    result.append([3])
                    for i in range(4, 3): no for loop
                print(result) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]