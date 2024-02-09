# 226. Invert binary tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Solution 1.
        if root is None:
            return root
        else:
            new_treenode = TreeNode(root.val)
            new_treenode.left = self.invertTree(root.right)
            new_treenode.right = self.invertTree(root.left)
        return new_treenode
    
        # Solution 2.
        if root is None:
            return root
        temp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(temp)
        return root
    
        # wrong
        # current = root
        # current.left = self.invertTree(root.right)
        # current.right = self.invertTree(root.left)
        # return current