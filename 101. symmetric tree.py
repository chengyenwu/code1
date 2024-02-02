# 101. Symmetric tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        
        node1 = root.left
        node2 = root.right
        return dfs(node1, node2)