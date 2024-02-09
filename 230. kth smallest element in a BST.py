# 230. Kth smallest element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 用inorder traversal把element 從小到大放入list中，再抓出k-1(index)的element，because k starts from 1 (1-indexed)
        def inorder(root):
            if root == None:
                return None
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)
        
        traversal=[]
        inorder(root)
        return traversal[k-1]