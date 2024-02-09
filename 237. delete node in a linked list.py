# 237. Delete node in a linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        # recording
        # 4 -> 5 -> 1 -> 9 ,and if node = 5
        # first let the node value equal to the next node value (4 -> 1 -> 1 ->9)
        # secondly, cut the next node link (4 -> 1 -> *1 (should be cut) -> 9  ==> 4 -> 1 -> 9)