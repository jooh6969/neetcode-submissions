# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        elif not list1:
            return list2
        elif not list2:
            return list1
        list1Head = list1.val
        list2Head = list2.val
        if list1Head < list2Head:
            return ListNode(
                list1Head,
                self.mergeTwoLists(list1.next, list2)
            )
        else:
            return ListNode(
                list2Head,
                self.mergeTwoLists(list1, list2.next)
            )