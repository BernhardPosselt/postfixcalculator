import re


class PostFixCalculator:

    def calculate(self, term):
        stack = []
        tokens = term.split(' ')

        result = None

        for token in tokens:
            if token == '':
                continue  # ignore empty tokens
            elif self.is_digit(token):
                token = self.cast(token)
                stack.append(token)
            elif token in '+-/*':
                action = None
                if token == '+':
                    action = lambda x, y: y + x # pop reverses the order
                elif token == '-':
                    action = lambda x, y: y - x

                result = action(stack.pop(), stack.pop())

        return result


    def is_digit(self, value):
        return re.match(r'^[-+]?\d+$', value)


    def cast(self, value):
        return float(value) if '.' in value else int(value)

