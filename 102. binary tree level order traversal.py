# 102. Binary tree level order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Recursive
        def bfs(root, level, travel):
            if root == None:
                return []
            if len(travel) < level+1:
                travel.append([])
            travel[level].append(root.val)
            bfs(root.left, level+1, travel)
            bfs(root.right, level+1, travel)
        
        level=0
        travel=[]
        bfs(root, level, travel)
        return travel
    
        # Iterative
        q = [root]
        res=[]
        while q:
            row=[]
            length = len(q)
            for i in range(length):
                curr = q.pop(0)
                row.append(current.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(row)
        return res