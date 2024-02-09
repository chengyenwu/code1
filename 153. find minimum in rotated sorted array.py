# 153. Find minimum in rotated sorted array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution 1. merge sort method
        def mergesort(array):
            if len(array)>1:
                r=len(array)//2
                left=array[:r]
                right=array[r:]
                mergesort(left)
                mergesort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i+=1
                    elif right[j] < left[i]:
                        array[k] = right[j]
                        j+=1
                    k+=1
                while i<len(left):
                    array[k] = left[i]
                    i+=1
                    k+=1
                while j<len(right):
                    array[k] = right[j]
                    j+=1
                    k+=1
        
        mergesort(nums)
        return nums[0]

        # Solution 2. binary search
        low = 0
        high = len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[high]>nums[mid]:
                high=mid
        return nums[low]