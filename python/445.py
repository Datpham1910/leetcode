"""
445. Add Two Numbers II
Medium

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t = l1
        n1 = 0
        while t:
            n1 = n1 * 10 + t.val
            t = t.next
        
        t = l2
        n2 = 0
        while t:
            n2 = n2 * 10 + t.val
            t = t.next
        n = n1 + n2
        trav = dummy = ListNode(0)
        while n:
            node = ListNode(n % 10)
            node.next, dummy.next = dummy.next, node
            n = n // 10
            
        return dummy.next or dummy

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        O(1) Space and O(N) Time (where N is the number of digits in the sum of the two given numbers.

        Process: Given two integers represented as Linked Lists, first convert them to integers, add them, then then their sum into a Linked List where each node carries one digit of the sum.

        Without altering the linked lists or using more space, we can obtain the parameter integers by using the formula:

        num = num*10 + nextvalue

        Where next value is just each of the values stored in each node of the linked lists.

        Convert the sum into a string, and use string manipulation to remove the first index to display the numbers in order as a linked list.
        """
        num1,num2 = 0,0
        while(l1):
            num1 = (num1*10 + l1.val)
            l1 = l1.next
        while(l2):
            num2 = (num2*10 + l2.val)
            l2 = l2.next
        
        s = str(num1+num2)
        
        head = ListNode(None)
        p = head
        while(s):
            new_node = ListNode(int(s[0]))
            head.next = new_node
            head = head.next
            s = s[1:]
        return p.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num3 = str(int(num1) + int(num2))
        head = None
        for digit in reversed(num3):
            head = ListNode(digit, head)
        return head