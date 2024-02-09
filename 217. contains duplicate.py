# 217. Contains duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [7, 6, 2, 3, 1, 7]
        s = set(nums)
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

        # import collections
        # c = collections.Counter(nums)
        # pair = c.most_common()[0]
        # times = pair[-1]
        # if times == 1:
        #     print('True')
        # else:
        #     print('False')