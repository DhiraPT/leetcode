# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        head2 = ListNode(0)
        head2.next = head
        node, prev = head, head2

        while node:
            if node.val in nums:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return head2.next