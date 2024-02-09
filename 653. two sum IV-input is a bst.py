# 653. Two sum IV-input is a bst
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # 先用inorder traversal建出list，再用two pointer尋找符合加起來的答案。
        def inorder(node):
            if node:
                inorder(node.left)
                travel.append(node.val)
                inorder(node.right)
        travel=[]
        inorder(root)
        
        left = 0
        right = len(travel)-1
        while left < right:
            if travel[left] + travel[right] == k:
                return True
            elif travel[left] + travel[right] < k:
                left+=1
            else:
                right-=1
        return False