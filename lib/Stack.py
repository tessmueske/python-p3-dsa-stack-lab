class Stack:

    def __init__(self, items = None, limit = None):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            print("Stack is full")
            return
        self.items.append(item)
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.limit == len(self.items):
            return True

    def search(self, target):
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        return -1

    def pop(self):
        if len(self.items) != 0:
            x = self.items.pop(-1)
            return x

    def peek(self):
        pass