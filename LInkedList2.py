class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.next = None
            item.prev = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        if self.head is None:
            pass
        elif self.head.value == val and self.head.next is None:
            self.clean()
        node = self.head
        while node is not None:
            if node.value == val and node.prev is None:
                self.head = self.head.next
                self.head.prev = None
                if not all:
                    break
            elif node.value == val and node.next is None:
                self.tail = self.tail.prev
                self.tail.next = None
                if not all:
                    break
            elif node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None or afterNode.next is None:
            self.add_in_tail(newNode)
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
        elif self.head.next is None:
            self.head = newNode
            self.head.next = self.tail
            self.head.prev = None
            self.tail.prev = self.head
        else:
            self.head.next.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.head.prev = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count
