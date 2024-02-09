# 31. Next permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first smaller number than the rightest number (or the righest)
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        # switch this number with the smallest number on its right side
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        # Finally, swap the two numbers on the right side of this number
        left = i+1
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1