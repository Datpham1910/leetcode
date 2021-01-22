"""
160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

begin to intersect at node c1.

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        This problem could be considered as the derivation of linked list cycle.
        Let say there are two linked lists named l1 and l2. And h1 and t1 are the head and last nodes of l1 respectively, and h2 is the head node of l2.

        Concat h1 and t1
        Check whether there exists a cycle of linked list l2.
        Find that intersection if 2 is a truth.
        Before doing the above steps, there are two linked lists in the picture:
        Before doing the above steps, there are two linked lists in the picture: ![enter image description here][1]

        After step 1:
        After step 1: ![enter image description here][2]

        Then let's try to make the linked lists easier to understood.
        Then let's try to make the linked lists easier to understood. ![enter image description here][3] Node 8 is what we want. We can use then solve it by finding the start node of the cycle like the problem "linked list cycle II"
        Node 8 is what we want. We can use then solve it by finding the start node of the cycle like the problem "linked list cycle II"
        """
        if not headA or not headB:
            return None

        p = headA
        while p.next:
            p = p.next
        mark = p
        #make a cycled list
        mark.next = headA

        rst = None
        p1 = headB
        p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
            if p1 == p2:
                break

        if p1 and p2 and p1 == p2:
            p1 = headB
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            rst = p1

        #unmake the cycle
        mark.next = None

        return rst

    
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Suppose there are two linked lists A and B with an intersection I starting at node X. The length of intersection is L, A's length is L1+L and B's is L2+L.
        
        And we have two pointers, a and b, walk through A and B in such way that a first walks through A then switch to B while b first walks through B then switch to A.

        In such manner, when a and b have walked a distance of L1+L2+L, a has walked through |A|+|B-I| (L1+L+L2) and reaches X while b has walked through |B|+|A-I| (L2+L+L1) and reaches X as well. Therefore, both a and b points to the start node of intersection when they first meet each other (a == b).

        Meanwhile, if A and B has no intersection (L = 0), a reaches the end of B and b reaches the end of A. Both of them point to None (a==b==None), which is also what to return. So we can combine two cases in such way:

        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
        # The time complexity is O(L1+L2+L) and space complexity if O(1)

if __name__ == "__main__":
    print(getIntersectionNode(listA = ListNode([4,1,8,4,5]), listB = ListNode([5,6,1,8,4,5])))