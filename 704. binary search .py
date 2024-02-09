# 704. Binary search 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        target = -1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if target == nums[mid]:
                break
            elif target > nums[mid]:
                low = mid+1
            else:
                high = low-1
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1