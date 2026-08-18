# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        L = dummy
        R = head

        i = 1

        while i <= n:
            R = R.next
            i = i + 1

        while R:
            L = L.next
            R = R.next

        temp = L.next
        L.next = temp.next

        return dummy.next