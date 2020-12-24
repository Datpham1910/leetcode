"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        head = ListNode(0)
        current = head

        i = l1
        j = l2

        while i and j:
            i_val = i.val
            j_val = j.val

            if i_val < j_val:
                current.next = ListNode(i_val)
                i = i.next
            else:
                current.next = ListNode(j_val)
                j = j.next

            current = current.next
        if i:
            current.next = i
        if j:
            current.next = j

        return head.next
