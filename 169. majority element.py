# 169. Majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import collections
        c = collections.Counter(nums)
        maxpair = c.most_common()[0]
        maxvalue = maxpair[0]
        return maxvalue