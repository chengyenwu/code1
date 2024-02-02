# 33. Search in rotated sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search method
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]: # left sorted part
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else: # right sorted part
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1