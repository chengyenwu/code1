# 136. Single number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [4,1,2,1,2]
        for i in nums:
            if nums.count(i) == 1:
                return i
            
        # import collections
        # c = collections.Counter(nums)
        # singlenum = c.most_common()[-1]
        # singlenumvalue = singlenum[0]
        # print(singlenumvalue)