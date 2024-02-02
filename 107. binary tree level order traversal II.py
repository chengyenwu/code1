# 107. Binary tree level order traversal II
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, travel):
            if root == None:
                return []
            # 如果travel list裡的元素比層數+1小，就在travel list裡面增加[]元素
            if len(travel) < level+1:
                travel.append([])
            # 同一層的node增加數字進去travel list裡
            travel[level].append(root.val)
            dfs(root.left, level+1, travel)
            dfs(root.right, level+1, travel)
            
        level=0
        travel=[]
        dfs(root, level, travel)
        return travel[::-1]