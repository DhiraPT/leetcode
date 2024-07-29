/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int c = 0;
        ListNode l3 = new ListNode(0);
        ListNode l4 = l3;
        while (l1 != null || l2 != null) {
            int s = c;
            if (l1 != null) {
                s += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                s += l2.val;
                l2 = l2.next;
            }
            c = s / 10;
            l4.next = new ListNode(s % 10);
            l4 = l4.next;
        }
        if (c > 0) {
            l4.next = new ListNode(c);
        }
        return l3.next;
    }
}
