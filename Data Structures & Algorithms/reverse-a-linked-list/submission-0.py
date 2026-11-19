# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = head
        current = prev.next
        while current is not None:
            right = current.next
            current.next = prev
            prev = current
            current = right
        head.next = None
        return prev

        
        