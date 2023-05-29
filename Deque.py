class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.insert(0, item)

    def addTail(self, item):
        self.queue.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        remove = self.queue[0]
        self.queue.remove(remove)
        return remove

    def removeTail(self):
        if self.size() == 0:
            return None
        remove = self.queue[self.size() - 1]
        self.queue.pop(self.size() - 1)
        return remove

    def size(self):
        return len(self.queue)
