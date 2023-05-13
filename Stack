class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        element = self.stack[self.size() - 1]
        self.stack.remove(element)
        return element

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[self.size() - 1]
