# 88. Merge sorted array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1=[-1,3,3,3,0,0,0,0,0]
        nums2 = [1,2,2]
        m=4
        n=3
        i = m-1 # index of nums1
        j = n-1 # index of nums2
        k = m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                print(i, 'before:', nums1)
                nums1[k] = nums1[i]
                print(i, 'after:', nums1)
                i-=1
                k-=1
            else:
                print(i, 'before:', nums1)
                nums1[k] = nums2[j]
                print(i, 'after:', nums1)
                j-=1
                k-=1
        nums1.sort()
        print(nums1)

        # for j in range(n):
        #     nums1[m+j] = nums2[j]
        # nums1.sort()