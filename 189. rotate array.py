# 189. Rotate array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using remainder , and rearranging the array 
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        # Solution 2. insert at the first position, and pop the last element
        # while k > 0:
        #     nums.insert(0, nums[-1])
        #     nums.pop()
        #     k-=1