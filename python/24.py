"""
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
 

Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        node = dummy.next
        prev = dummy

        while node and node.next:
            tmp = node.next
            node.next = tmp.next
            tmp.next = node
            prev.next = tmp
            prev = node
            node = node.next

        return dummy.next

    def swapPairs1(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        # if at least 2 nodes
        if head and head.next:
            p2 = head.next
        else:
            return head

        while True:
            head.val, p2.val = p2.val, head.val

            if p2.next and p2.next.next:
                head = p2.next
                p2 = p2.next.next
            else:
                break

        return head


if __name__ == "__main__":
    print(Solution().swapPairs2(head = ListNode([1,2,3,4])))
    print(Solution().swapPairs1(head = ListNode([1,2,3,4])))
    print(Solution().swapPairs(head = ListNode([1,2,3,4])))