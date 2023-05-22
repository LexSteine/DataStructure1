class Queue:
    def __init__(self):
        self.qu = []

    def enqueue(self, item):
        self.qu.insert(0, item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.qu.pop()

    def size(self):
        return len(self.qu)
