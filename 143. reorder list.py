# 143. Reorder list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Find the middle node
        second = slow.next
        # Totally cut the linked list
        slow.next = None
        
        # Reverse the second half linked list
        prev = None
        while second:
            curr = second
            second = second.next
            curr.next = prev
            prev = curr
        
        # Combined two lists
        head1 = head
        head2 = prev
        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2