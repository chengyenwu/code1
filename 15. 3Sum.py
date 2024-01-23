# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        # [-4, -1, -1, 0, 1, 2]
        result=[]
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # consider left and left+1 have the same value (ex: [-2, 0, 0, 2, 2])
                    while left+1 < right and nums[left] == nums[left+1]:
                        left+=1
                    # consider right and right-1 have the same value (ex: [-2, 0, 0, 2, 2])
                    while right-1 > left and nums[right-1] == nums[right]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left+=1
        return result