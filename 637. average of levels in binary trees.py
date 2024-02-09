# 637. Average of levels in binary trees
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans=[]
        q=[root]
        while q:
            temp=[]
            s=float(0)
            for i in q:
                s += i.val
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            ans.append(float(s / len(q)))
            q=temp
        return ans