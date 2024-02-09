# 206. Reversed linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # list = [1 -> 2 -> 3]
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev

# c: 1
# h: 2
# 1 -> none
# p: 1

# c: 2
# h: 3
# 2 -> 1 -> none
# p: 2

# c: 3
# h: none
# 3 -> 2  -> 1 -> none
# p: 3