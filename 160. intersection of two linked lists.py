# 160. Intersection of two linked lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # two pointer in two linked list, and if going to the end, the next node is the first node in the other linked list
        h1 = headA
        h2 = headB
        while h1 != h2:
            if not h1:
                h1 = headB
            else:
                h1 = h1.next
            if not h2:
                h2 = headA
            else:
                h2 = h2.next
        return h1