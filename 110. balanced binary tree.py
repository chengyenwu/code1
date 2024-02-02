# 110. Balanced binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def DFS(root):
            if not root:
                return 0
            left = DFS(root.left)
            right = DFS(root.right)
            return max(left, right)+1

        left_depth = DFS(root.left)
        right_depth = DFS(root.right)
        if abs(left_depth - right_depth) >= 2:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)