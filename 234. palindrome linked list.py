# 234. Palindrome linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 找到linkedlist一半的位置 = slow的node
        fast = head
        slow = head 
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next

        # 把linked list後半部分反轉，temp為一半list的下一個node
        prev = None
        while slow: 
            temp = slow.next 
            slow.next = prev
            prev = slow 
            slow = temp
 
        while prev: 
            if head.val != prev.val: 
                return False 
            head = head.next 
            prev = prev.next 
        return True
    
        # reverseListNode = ListNode(head.val)
        # node = head
        # while node:
        #     current = ListNode(node.val)
        #     node = node.next
        #     current.next = reverseListNode
        #     reverseListNode = current
            
        # while head and reverseListNode:
        #     if head.val != reverseListNode.val:
        #         return False
        #     head = head.next
        #     reverseListNode = reverseListNode.next
        # return True