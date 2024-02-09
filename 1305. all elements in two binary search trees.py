# 1305. All elements in two binary search trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # inorder traversal, and merge two list in ascending sorted
        def inorder(node, travel):
            if node == None:
                return None
            inorder(node.left, travel)
            travel.append(node.val)
            inorder(node.right, travel)
        
        list1=[]
        list2=[]
        inorder(root1, list1)
        inorder(root2, list2)
        result = list1 + list2
        result.sort()
        return result