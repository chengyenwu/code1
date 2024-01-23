# 11. Container with most water 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer method
        left = 0
        right = len(height)-1
        area = 0
        while left < right:
            vertical_height = min(height[left], height[right])
            area = max(area, vertical_height * (right-left))
            if height[left] <= height[right]:
                left+=1 
            else: 
                right-=1
        return area