# 1. Two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]        
        # nums = [2, 9, 7, 1, 10, 4]
        # target = 9
        # length = len(nums)
        # for a in range(length):
        #     for b in range(a+1, length):
        #         if a != b and nums[a] + nums[b] == target:
        #             print([a, b])