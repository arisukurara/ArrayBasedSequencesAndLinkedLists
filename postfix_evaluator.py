from stack import Stack

class PostfixEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.stack = Stack()

    def evaluate(self):
        tokens = self.expression.split()
        for token in tokens:
            if token.replace('.', '', 1).lstrip('-').isdigit():
                self.stack.push(float(token))
            else:
                right = self.stack.pop()
                left = self.stack.pop()
                if token == '+':
                    self.stack.push(left + right)
                elif token == '-':
                    self.stack.push(left - right)
                elif token == '*':
                    self.stack.push(left * right)
                elif token == '/':
                    self.stack.push(left / right)
                elif token == '^':
                    self.stack.push(left ** right)
        return self.stack.pop()