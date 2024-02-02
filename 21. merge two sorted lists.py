# 21. Merge two sorted lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = ListNode(-1)
        head = current
        while list1 or list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return head.next
    
# return 起點的下一個點開始
# list1: [1,2,4]
# list2: [1,3,4]
# c: listnode(-1)
# h: listnode(-1)
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4

# listnode(-1) -> 1 -> 2 -> 4
# list1: 2 -> 4
# c: 1

# 1 -> 1 -> 3 -> 4
# list2: 3 -> 4
# c: 1

# 1 -> 2 -> 4
# list1: 4
# c: 2

# 2 -> 3 -> 4
# list2: 4
# c: 3

# 3 -> 4
# list1: none
# c: 4

# 4 -> 4
# list2: None
# c: 4