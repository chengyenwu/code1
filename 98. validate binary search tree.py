# 98. Validate binary search tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Solution  1.
        # 使用system integer代表infinity
        inf = sys.maxsize 

        def dfs(root, minlimit, maxlimit):
            if not root:
                return True
            if minlimit < root.val < maxlimit:
                return dfs(root.left, minlimit, root.val) and dfs(root.right, root.val, maxlimit)
            else:
                return False
        return dfs(root, -inf, inf)
        
        # solution 2. 使用inorder travesal把每個node數字紀錄並前後比大小
        def inorder(root):
            if root == None:
                return None
            inorder(root.left)
            travel.append(root.val)
            inorder(root.right)
        
        travel=[]
        inorder(root)
        for i in range(len(travel)-1):
            if travel[i] >= travel[i+1]:
                return False
        return True