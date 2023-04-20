class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        prev = None
        while node is not None:
            if node.value == val and prev is None:
                if self.head.next is None:
                    self.clean()
                else:
                    self.head = self.head.next
                node = self.head
                if not all:
                    break
            elif node.value == val and node.next is None:
                self.tail = prev
                prev.next = None
                break
            elif node.value == val and node.next is not None:
                node.value = node.next.value
                node.next = node.next.next
                if not all:
                    break
            else:
                prev = node
                node = node.next
        pass

    def clean(self):
        self.head = None
        self.tail = None
        pass

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
        elif afterNode is None:
            newNode.next = self.head
            self.head = newNode
        elif afterNode.next is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
        pass
