# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        first = 0
        while l1:
            first += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        j = 0
        second = 0
        while l2:
            second += l2.val * (10 ** j)
            l2 = l2.next
            j += 1
        total = first + second
        tmp = ListNode(0)
        if total == 0:
            return tmp
        ptr = tmp
        while total:
            digit = total % 10
            total = total // 10
            ptr.next = ListNode(digit)
            ptr = ptr.next
        return tmp.next            



