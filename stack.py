class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise Exception("Stack is empty") 

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise Exception("Stack is empty") 

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def size(self):
        return len(self.stack)