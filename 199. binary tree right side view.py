# 199. Binary tree right side view
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive method
        def bfs(node, level, travel):
            if node == None:
                return None
            if node and level == len(travel):
                travel.append(node.val)
            bfs(node.right, level+1, travel)
            bfs(node.left, level+1, travel)
        travel=[]
        level=0
        bfs(root, level, travel)
        return travel