# 222. Count complete tree nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int: 
        self.k = 0
        def inorder(root):
            if root == None:
                return 0
            if root:
                inorder(root.left)
                self.k+=1
                inorder(root.right)
        inorder(root)
        return self.k