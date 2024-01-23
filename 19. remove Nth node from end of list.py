# 19. Remove Nth node from end of list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # linked list(two pointer method)
        k=1
        fast=head
        slow=head
        current=head
        while k<=n:
            fast = fast.next
            k+=1
        # deleting the first node(only one node)
        if fast == None:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return current
