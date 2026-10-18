# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head.next
        length = 1
        while tmp:
            length += 1
            tmp = tmp.next
        # [1,2,3,4,5,6,7], n = 5
        # want to remove (length - n)th node
        position = length - n
        if position == 0:
            if length == 1:
                return None
            else:
                return head.next
        ptr = head
        for i in range(position - 1):
            ptr = ptr.next
        # this lands us 1 before the position to remove
        rmv = ptr.next
        if rmv.next:
            ptr.next = rmv.next
        else:
            ptr.next = None
        return head
