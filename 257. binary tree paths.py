# 257. Binary tree paths
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        print(left_paths)
        print(right_paths)
        left = [str(root.val) + "->" + node for node in left_paths]
        right = [str(root.val) + "->" + node for node in right_paths]
        return left + right
        
        # recording
        # f(1, left)=node2
        #     f(2,left)=none
        #     f(2,right)=node5
        #         f(5,left)=none
        #         f(5,right)=none -> return str(5)
        #     print(2, l, [])
        #     print(2, r, [5])
        #     left = [str(2)->[]] = none
        #     right = [str(2)->str(5)] -> return [str(2)->str(5)]
        # f(1, right)=node3
        #     f(3, left)=none
        #     f(3, right)=none -> return str(3)
        # print(1, l, [str(2)->str(5)])
        # print(1, r, [3])
        # left = [str(1)->str(2)->str(5)]
        # right = [str(1)->str(3)]