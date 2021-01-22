"""
234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        ## RC ##
        ## APPROACH : similar to reverse linked list ##
        #   1. First make a copy of LL.
        #   2. use fast and slow to find middle of LL #(now slow has second half of LL)
        #   3. now reverse slow LL and compare with first half of original copy.
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        #EDGE CASE
        if(not head or not head.next):return True                   #Edge Case
        
        slow=fast=head                                              #1. SLOW AND FAST(GO TO MID with SLOW)
        while(fast and fast.next):
            slow=slow.next
            fast = fast.next.next
             
        
        #2. REVERSE SLOW LL
        # LOGIC : 3->2->1
        #1. CREATE A REV node with first VALUE.
        #2. ITERATE
        #3. COPY REV TO PREVIOUS # COZ we have to concatinate the prev rev chain to current 
        #4. CONCAT PREV TO CURR NODE # not curr to prev
        #5. 
        rev=ListNode(slow.val)
        slow=slow.next
        while(slow):
            prev=rev                                                # IMP STEP # USE PREVIOUS
            curr = ListNode(slow.val)
            curr.next = prev
            rev=curr
            slow=slow.next
            
        while(rev):
            if(rev.val!=head.val):
                return False
            rev=rev.next
            head=head.next
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        # reverse left half of the list while searching
        # the start point of the right half
        while fast is not None and fast.next is not None:
            tmp = slow

            # keep moving guys
            slow = slow.next
            fast = fast.next.next

            # place node at the start of the reversed half
            tmp.next = reversed_list
            reversed_list = tmp

        # if there are even number of elements in the list
        # do one more step to reach the first element of
        # the second list's half
        if fast is not None:
            slow = slow.next

        # compare reversed left half with the original
        # right half
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return reversed_list is None