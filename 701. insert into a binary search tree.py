# 701. Insert into a binary search tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        def dfs(node, k):
            if k > node.val:
                if node.right == None:
                    node.right = TreeNode(k)
                else:
                    dfs(node.right, k)
            elif k < node.val:
                if node.left == None:
                    node.left = TreeNode(k)
                else:
                    dfs(node.left, k)

        dfs(root, val)
        return root