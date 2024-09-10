# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        prev, curr = head, head.next
        while curr:
            gcd = ListNode(math.gcd(prev.val, curr.val), curr)
            prev.next = gcd
            prev = curr
            curr = curr.next

        return head