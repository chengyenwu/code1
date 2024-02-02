# 94. Binary tree inorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive
        inorderlist=[]
        def inorder(node):
            if node:
                inorder(node.left)
                inorderlist.append(node.val)
                inorder(node.right)
        inorder(root)
        return inorderlist
    

        # iterative
        visit = []
        if not root:
            return visit
        
        temp = []
        current = root
        while current or temp:
            if current:
                temp.append(current) # temp儲存節點而非值
                current = current.left
            else:
                current = temp.pop()
                visit.append(current.val) #visit列表儲存值
                current = current.right
        return visit