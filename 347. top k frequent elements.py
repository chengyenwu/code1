# 347. Top K frequent elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using collections.Counter
        result=[]
        import collections
        c = collections.Counter(nums)
        pairs = c.most_common()
        for i in range(k):
            result.append(pairs[i][0])
        return result