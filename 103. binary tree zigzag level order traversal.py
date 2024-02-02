# 103. Binary tree zigzag level order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursive (using bfs method)
        def bfs(node, level, travel):
            if node == None:
                return None
            if level % 2 == 0:
                if len(travel)<level+1:
                    travel.append([])
                travel[level].append(node.val)          
            elif level % 2 == 1:
                if len(travel)<level+1:
                    travel.append([])
                travel[level].insert(0, node.val)
            bfs(node.left, level+1, travel)
            bfs(node.right, level+1, travel)

        travel=[]
        level=0
        bfs(root, level, travel)
        return travel