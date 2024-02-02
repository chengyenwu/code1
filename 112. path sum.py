# 112. Path sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, target):
            if root == None:
                return False
            target = target - root.val
            if not root.left and not root.right:
                return target == 0
            return dfs(root.left, target) or dfs(root.right, target)
        return dfs(root, targetSum)
        
        #　Solution 2.
        if root == None:
            return False
        target = targetSum - root.val
        if root.left == None and root.right == None:
            return target == 0
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)