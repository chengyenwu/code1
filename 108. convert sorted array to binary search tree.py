# 108. Convert sorted array to binary search tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = (len(nums))//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
        # wrong method
        # if not nums:
        #         return None
        #     low = 0
        #     high = len(nums)-1
        #     mid = (low+high)//2
        #     new_tree = TreeNode(nums[mid])
        #     for i in range(mid-1, -1, -1):
        #         new_tree.left = TreeNode(nums[i])
        #     for j in range(mid+1, len(nums)-1):
        #         new_tree.right = TreeNode(nums[j])
        #     return new_tree