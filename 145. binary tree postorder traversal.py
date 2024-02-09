# 145. Binary tree postorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if root == None:
                return None
            if node:
                postorder(node.left)
                postorder(node.right)
                travel.append(node.val)
                
        travel=[]
        postorder(root)
        return travel