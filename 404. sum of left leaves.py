# 404. Sum of left leaves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, k):
            if node == None:
                return 0
            if node.left and not node.left.left and not node.left.right:
                self.k+=node.left.val
            return dfs(node.left, k) + dfs(node.right, k)    

        self.k=0
        dfs(root, self.k)
        return self.k