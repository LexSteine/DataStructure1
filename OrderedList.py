class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value == v2.value:
            return 0
        if v1.value > v2.value:
            return 1
        return -1

    def add(self, value):
        node = Node(value)
        if self.compare(node, self.tail) >= 0 and self.__ascending is True:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            pass
        if self.compare(node, self.head) <= 0 and self.__ascending is True:
            self.head.prev = node
            node.next = self.head
            self.head = node
            pass
        if self.compare(node, self.head) >= 0 and self.__ascending is False:
            self.head.prev = node
            node.next = self.head
            self.head = node
            pass
        if self.compare(node, self.tail) <= 0 and self.__ascending is False:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            pass
        orderNode = self.head.next
        while self.__ascending is True and orderNode.next is not None:
            if node.value <= orderNode.value:
                node.prev = orderNode.prev
                node.next = orderNode
                orderNode.prev.next = node
                orderNode.prev = node
            orderNode = orderNode.next
        while self.__ascending is False and orderNode.next is not None:
            if node.value >= orderNode.value:
                node.prev = orderNode.prev
                node.next = orderNode
                orderNode.prev.next = node
                orderNode.prev = node
            orderNode = orderNode.next
        pass
        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        if self.__ascending and self.head.value > val or self.tail.value < val:
            return None
        if not self.__ascending and self.head.value < val or self.tail.value > val:
            return None
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val, all=False):
        if self.head is None:
            pass
        elif self.head.value == val and self.head.next is None:
            self.clean(self.__ascending)
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
        pass

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # s1 = v1.value
        if v1.value.strip() == v2.value.strip():
            return 0
        if v1.value.strip() > v2.value.strip():
            return 1
        return -1
