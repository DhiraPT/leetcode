# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        q, r = divmod(N, k)

        res = []
        curr = head
        for i in range(k):
            if i < r:
                length = q + 1
            else:
                length = q

            if length == 0:
                res.append(None)
            else:
                part_head = curr
                while length > 1:
                    curr = curr.next
                    length -= 1
                if curr:
                    next_part = curr.next
                    curr.next = None
                    curr = next_part
                res.append(part_head)

        return res