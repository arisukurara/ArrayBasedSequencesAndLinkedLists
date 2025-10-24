from stack import Stack

class InfixConverter:
    def __init__(self, expression):
        self.expression = expression
        self.stack = Stack()
        self.output = []
        self.prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
        self.right_assoc = {'^'}

    def convert(self):
        for tok in self.expression.split():
            if tok not in self.prec and tok not in {'(', ')'}:
                self.output.append(tok)
            elif tok == '(':
                self.stack.push(tok)
            elif tok == ')':
                while self.stack.peek() != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()
            else:
                while (not self.stack.is_empty() and self.stack.peek() != '(' and
                       (self.prec.get(self.stack.peek(), 0) > self.prec[tok] or
                        (self.prec.get(self.stack.peek(), 0) == self.prec[tok] and tok not in self.right_assoc))):
                    self.output.append(self.stack.pop())
                self.stack.push(tok)
        while not self.stack.is_empty():
            self.output.append(self.stack.pop())
        return ' '.join(self.output)