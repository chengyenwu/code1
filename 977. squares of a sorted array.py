# 977. Squares of a sorted array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointer method
        square_list=[]
        low = 0
        high = len(nums)-1
        while low <= high:
            leftsquare = nums[low]**2
            rightsquare = nums[highj]**2
            if leftsquare > rightsquare:
                square_list.insert(0, leftsquare)
                low+=1
            else:
                square_list.insert(0, rightsquare)
                high-=1
        return square_list
    
        result_list = [0] * len(nums)
        l = 0
        r = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l]) <= abs(nums[r]):
                square_number = nums[r] ** 2
                r-=1
            else:
                square_number = nums[l] ** 2
                l+=1
            result_list[i] = square_number
        return result_list