class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# hanoi = Node('Ha Noi')
# qb = Node('Quang Binh')
# dn = Node('Da Nang')
# sg = Node('Sai Gon')

# hanoi.next = qb
# qb.next = dn
# dn.next = sg


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def placeOnTop(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def insert(self, target, value):
        node = Node(value)
        node.next = target.next
        target.next = node

    def delete(self, value):
        current = self.head
        if value == self.head.value:
            self.head = current.next
            current = None
            return
        pre = None
        while current:
            if current.value == value:
                break
            pre = current
            current = current.next
        print('===========')
        print(pre.value)
        pre.next = current.next
        current = None




linked_list = LinkedList()
linked_list.head = Node('Hà Nội')
second = Node('Quảng Bình')
third = Node('Đà Nẵng')
fourth = Node('Sài Gòn')

linked_list.head.next = second
second.next = third
third.next = fourth

linked_list.placeOnTop('Hà Giang')
linked_list.append('Cà Mau')
linked_list.delete('Quảng Bình')


linked_list.printList()
