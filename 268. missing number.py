# 268. Missing number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k = 0
        for i in range(len(nums)):
            if k == nums[i]:
                k+=1
            else:
                break
        return k