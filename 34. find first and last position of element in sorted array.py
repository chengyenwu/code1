# 34. Find first and last position of element in sorted array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Two pointer method
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
        left=0
        right=len(nums)-1
        if nums == None:
            return [-1, -1]
        while left <= right:
            if nums[right] > target:
                right-=1
            elif nums[left] < target:
                left+=1
            elif nums[left] == target and nums[right] == target:
                return [left, right]
        return [-1, -1]

        # Ideally, we should solve this problem with binary search (O(log n))