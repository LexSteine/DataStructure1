class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):        
        summa = len(value.encode('utf8'))
        return summa % self.size

    def seek_slot(self, value):        
        hashStep = self.step
        hash = self.hash_fun(value)
        if self.slots[hash] is None:
            return hash
        nextIteration = False
        while self.slots[hash] is not None:
            hash += hashStep
            if hash >= len(self.slots):
                hash = hash - len(self.slots)
                nextIteration = True
                hashStep *= 2
            if nextIteration and hash > self.hash_fun(value):
                return None
            if nextIteration and hash + self.step >= len(self.slots):
                return None
        return hash

    def put(self, value):  
        index = self.seek_slot(value)
        if index is None:
            return None
        self.slots[index] = value
        return index

    def find(self, value):       
        index = None
        for i in range(len(self.slots)):
            slot = self.slots[i]
            if slot is not None and slot == value:
                return i
        return index
