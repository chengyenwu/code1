# 1985. Find the kth largest integer in the array
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # heapify
        numslist=[]
        for i in range(len(nums)):
            heapq.heappush(numslist, int(nums[i]))
            if len(numslist) > k:
                heapq.heappop(numslist)
        return str(numslist[0])