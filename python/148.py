"""
148. Sort List
Medium

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        """
        This is pretty straightforward question, if you know how to use merge sort. All we need to do is to split our list into two parts, sort the first half, then sort the second half and finally merge this two parts. Here I use two axuilary function:

        getMid(head), which will find the middle of list with given head and cut it into two smaller lists. We use the idea of slow and fast pointers here to find middle efficiently.
        merge(head1, head2) will merge two lists with given heads. To make it more readible and to avoid corner cases, it is good idea to use dummy sentinel node in the beginning of list. We iterate over two lists, using two pointers and add them one by one. When we out of nodes, we attach the rest of on of the lists to the end, we return the start of our new list.
        sortList(head): it is our original function: if list has length 0 or 1, we do not do anything, it is corner case of our recursion. If it is not the case, we find mid = self.getMid(head), which will cut our list into two smaller lists and return the start of the second list. Finally, we apply sortList() to head and to mid and merge two parts.
        Complexity: Time complexity is O(n log n), because it is classical complexity of merge sort. Space complexity is O(log n), because we use recursion which can be log n deep.

        Follow up question askes us to do it in O(1) memory, and it is possible to do it, using bottom-up merge sort, which is much more difficult to implement during interview limits. What I expect that if you just explain the idea, without implementing this will be already quite good. So, idea is the following: imagine, that we have list a1, a2, a3, a4, a5, a6, a7, a8. Let us first sort values in pairs:
        (a1, a2), (a3, a4), (a5, a6), (a7, a8).
        then we sort values in groups by 4, mergin our pairs:
        (a1, a2, a3, a4), (a5, a6, a7, a8).
        And finally we merge them in one group of 9. It is more difficult to implement and I will add code later.
        """
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, head1, head2):
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next

        tail.next = head1 or head2
        return dummy.next
    

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # cut the list into two halves
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        
        return self.merge(l, r)
