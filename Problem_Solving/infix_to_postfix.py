class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, element):
        self.items.append(element)
        self.top += 1

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.items.pop()
        else:
            print("Stack is empty!")
            return None

    def is_empty(self):
        return self.top == -1

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]
        return None


class InfixToPostfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.postfix = ""

    def is_operand(self, ch):
        return ch.isalnum()

    def precedence(self, op):
        if op == '^':
            return 3
        elif op in ('*', '/'):
            return 2
        elif op in ('+', '-'):
            return 1
        return 0

    def convert(self, infix_expr):
        i = 0
        while i < len(infix_expr):
            char = infix_expr[i]

            if char == '*' and i + 1 < len(infix_expr) and infix_expr[i + 1] == '*':
                char = '^'
                i += 1

            if self.is_operand(char):
                self.postfix += char
            elif char == '(':
                self.stack.push(char)
            elif char == ')':
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    self.postfix += self.stack.pop()
                self.stack.pop()
            else:
                while (not self.stack.is_empty() and
                       self.precedence(char) <= self.precedence(self.stack.peek())):
                    self.postfix += self.stack.pop()
                self.stack.push(char)

            i += 1

        # Pop remaining operators
        while not self.stack.is_empty():
            self.postfix += self.stack.pop()

        return self.postfix


if __name__ == '__main__':
    infix_input = input("Enter infix expression: ")
    converter = InfixToPostfixConverter()
    postfix_output = converter.convert(infix_input)
    print("Postfix expression:", postfix_output)
