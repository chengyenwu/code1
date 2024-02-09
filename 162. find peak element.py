# 162. Find peak element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Two pointer method
        low=0
        high=len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return low

        # consider all situations
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] >= nums[1]:
                return 0
            else:
                return 1
        elif nums[0] == max(nums):
            return 0
        elif nums[-1] == max(nums):
            return len(nums)-1
        else:
            for i in range(1, len(nums)-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i