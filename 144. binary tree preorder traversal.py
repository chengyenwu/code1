# 144. Binary tree preorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Solution 1. recursive
        preorderlist=[]
        def preordertraversal(root, preorderlist):
            if root is not None:
                preorderlist.append(root.val)
                preordertraversal(root.left, preorderlist)
                preordertraversal(root.right, preorderlist)
        
        preordertraversal(root, preorderlist)
        return preorderlist
    
        # Solution 2. itreative
        # stack = []
        # result = []
        # current = root
        # while stack or current:
        #     if current:
        #         result.append(current.val)
        #         stack.append(current.right)
        #         current = current.left
        #     else:
        #         current = stack.pop()
        # return result
    
        # root = [1, NULL, 2, 3]
        # (c: root)
        # r: [1]
        # s: [2]
        # c: None

        # c: 2
        # (c:2)
        # r: [1, 2]
        # s: None
        # c: 3

        # (c:3)
        # r: [1, 2, 3]
        # s: None
        # c: None