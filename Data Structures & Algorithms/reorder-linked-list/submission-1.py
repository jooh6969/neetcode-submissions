# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if i can reverse the second half of the linked list, i can alternate the lists and pick out elements
        if not head or not head.next:
            return # trivial case
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # since fast moves twice the rate of slow, when it hits the end, slow will be at the middle
        second_half = slow.next # split
        slow.next = None # elem at middle position is the end of the list

        # next we reverse the second list
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        second = prev
        while second: # if length is odd, then first has 1 more than second
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        


