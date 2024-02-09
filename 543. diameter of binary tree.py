# 543. Diameter of binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1.
        def diameter(node):
            if node is None:
                return 0
            left = diameter(node.left)
            right = diameter(node.right)
            self.diameter = max(self.diameter, left+right)
            return 1 + max(left, right)
        self.diameter = 0
        diameter(root)
        return self.diameter
# recorfing
# l=f(1.l) => 2
#   l=f(2.l) => 1
#     l=f(4.l) => return 0
#     r=f(4.r) => return 0
#     self.d=max(0,0)=0
#     return 1+max(0,0)=1
#   r=f(2.r) => 1
#     l=f(5.l) => return 0
#     r=f(5.r) => return 0
#     self.d=max(0,0)=0
#     return 1+max(0,0)=1
#   self.d=max(0,2)=2
#   return 1+max(1,1)=2
# r=f(1.r) => 1
#   l=f(3.l) => return 0
#   r=f(3.r) => return 0
#   self.d=max(0,0)=0
#   return 1+max(0,0)=1
# self.d=max(0, 3)=3
# return 1+max(2,1)=3

# Solution 2.    
    #     if not root:
    #         return 0
    #     self.diameter = 0
    #     self.DFS(root)
    #     return self.diameter
    # def DFS(self, node):
    #     leftH, rightH = 0, 0
    #     if node.left:
    #         leftH = self.DFS(node.left) + 1
    #     if node.right:
    #         rightH = self.DFS(node.right) + 1
    #     self.diameter = max(self.diameter, leftH + rightH)
    #     return max(leftH, rightH)