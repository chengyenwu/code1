# 113. Path sum II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, target, travel):
            if root == None:
                return None
            target = target - root.val
            travel.append(root.val)
            if not root.left and not root.right and target == 0:
                result.append(travel.copy())
            dfs(root.left, target, travel)
            dfs(root.right, target, travel)
            travel.pop()
        
        result=[]
        travel=[]
        dfs(root, targetSum, travel)
        return result