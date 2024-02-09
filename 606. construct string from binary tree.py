# 606. Construct string from binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root == None:
                return None
            travel.append(str(root.val))
            if root.left == None and root.right == None:
                return None    
            travel.append('(')
            preorder(root.left)
            travel.append(')')
            
            if root.right != None:
                travel.append('(')
                preorder(root.right)
                travel.append(')')
        
        travel=[]
        preorder(root)
        return "".join(travel)