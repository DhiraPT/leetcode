# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow, fast = head, head
        prev_slow = None

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        prev_slow.next = slow.next

        return head