# 215. Kth largest element in an array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify
        result=[]
        for i in nums:
            heapq.heappush(result, i)
            if len(result) > k:
                heapq.heappop(result)
        return result[0]
        
        # Solution 2. mergesort
        # def mergesort(array):
        #     if len(array) == 1:
        #         return array[0]
        #     if len(array) > 1:
        #         mid = len(array)//2
        #         L = array[:mid]
        #         M = array[mid:]
        #         mergesort(L)
        #         mergesort(M)
        #         i = j = k = 0
        #         while i < len(L) and j < len(M):
        #             if L[i] <= M[j]:
        #                 array[k] = L[i]
        #                 i+=1
        #             else:
        #                 array[k] = M[j]
        #                 j+=1
        #             k+=1
        #         while i < len(L):
        #             array[k] = L[i]
        #             i+=1
        #             k+=1
        #         while j < len(M):
        #             array[k] = M[j]
        #             j+=1
        #             k+=1
        
        # mergesort(nums)
        # return nums[len(nums)-k]