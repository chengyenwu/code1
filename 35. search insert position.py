# 35. Search insert position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        low = 0
        high = len(nums)-1
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            while low<=high:
                mid = (low+high)//2
                if target < nums[mid]:
                    high = mid-1
                elif target == nums[mid]:
                    return mid
                else:
                    low = mid+1
            return low