# 109. Convert sorted list to binary search tree
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findmid(head):
            # two pointer
            if head == None or head.next == None:
                return head
            fast=head
            slow=head
            prev=None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            # cut the link between slow(middle point) and its previous point
            if prev:
                prev.next = None
            return slow # return middle point
        
        # if input linked list is empty, return None 
        if head == None:
            return None
        
        mid = findmid(head)
        root = TreeNode(mid.val)
        # consider situation that only one node is in linked list 
        if head == mid:
            return root
        # left tree is from head to the middle point, and the right tree is from the next point of middle point to the end
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root