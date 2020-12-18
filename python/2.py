# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         added = ListNode(val=(l1.val + l2.val) % 10)
#         carry_over = (l1.val + l2.val)//10
#         current_node = added

#         while (l1.next and l2.next):
#             l1 = l1.next
#             l2 = l2.next
#             current_node.next = ListNode(val=(carry_over + l1.val + l2.val) % 10)
#             carry_over = (carry_over + l1.val + l2.val) // 10
#             current_node = current_node.next

#         while (l1.next):
#             l1 = l1.next
#             current_node.next = ListNode(val=(carry_over + l1.val) % 10)
#             carry_over = (carry_over + l1.val) // 10
#             current_node = current_node.next

#         while (l2.next):
#             l2 = l2.next
#             current_node.next = ListNode(val=(carry_over + l2.val) % 10)
#             carry_over = (carry_over + l2.val) // 10
#             current_node = current_node.next
#         if carry_over > 0:
#             current_node.next = ListNode(val=1)

#         return added

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        new_list = ListNode(0)
        tmp = new_list
        total_sum = 0
        while l1 or l2 or carry:
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 =l2.next

            total_sum += carry
            carry = total_sum // 10
            tmp.next = ListNode(total_sum%10)
            total_sum = 0
            tmp = tmp.next
        return new_list.next