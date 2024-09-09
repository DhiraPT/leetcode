# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        r, c, dr, dc = 0, 0, 0, 1

        while head:
            matrix[r][c] = head.val
            head = head.next
            new_r, new_c = r + dr, c + dc
            if new_r >= m or new_r < 0 or new_c >= n or new_c < 0 or matrix[new_r][new_c] != -1:
                dr, dc = dc, -dr
            r += dr
            c += dc

        return matrix