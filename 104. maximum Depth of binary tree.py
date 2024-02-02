# 104. Maximum Depth of binary tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            elif node.left == None and node.right == None:
                return 1
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            return max(left, right)
        return dfs(root)
    

        # Solution 2.
        if root is None:
            return 0
        else:
            left = 1 + self.maxDepth(root.left) #利用recursion
            right = 1 + self.maxDepth(root.right)
        return max(left, right)