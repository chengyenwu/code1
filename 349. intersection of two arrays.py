# 349. Intersection of two arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        left=0
        right=0
        nums1.sort()
        nums2.sort()
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left+=1
            elif nums1[left] > nums2[right]:
                right+=1
            else:
                if nums1[left] not in result:
                    result.append(nums1[left])
                left+=1
                right+=1
        return result