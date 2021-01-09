"""
92. Reverse Linked List II
Medium

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

    def reverseBetween1(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        current = head

        # Move to the mth node in the linked list.
        i = 1
        while current and i < m:
            prev = current
            current = current.next
            i += 1

        start = current
        end = None

        # Reversing the elements from m - nth nodes in the linked list.
        while current and i <= n:
            temp = current.next
            current.next = end
            end = current
            current = temp
            i += 1

        start.next = current
        if prev is None:
            head = end
        else:
            prev.next = end

        return head
