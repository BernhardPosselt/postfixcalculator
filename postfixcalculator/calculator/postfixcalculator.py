import re

class MalformedTermException(Exception):
    pass


class PostFixCalculator:

    def tokenize(self, term):
        tokens = []
        tmp = ''
        for counter, token in enumerate(term):
            if token == ' ':
                if tmp != '':
                    tokens.append(tmp)
                    tmp = ''
            elif token in '+-*/~':
                if tmp != '':
                    tokens.append(tmp)
                    tmp = ''
                tokens.append(token)
            elif token in '0123456789.':
                tmp += token
                if counter+1 == len(term):
                    tokens.append(tmp)
            else:
                raise MalformedTermException('Token not recognized %s' % token)

        return tokens


    def calculate(self, term):
        stack = []
        original_term = ''.join(term)  # copy string for error message

        try:
            tokens = self.tokenize(term)

            for token in tokens:
                if token in '+-/*~':
                    if token == '+':
                        action = lambda x, y: y + x # pop reverses the order
                        stack.append(action(stack.pop(), stack.pop()))
                    elif token == '-':
                        action = lambda x, y: y - x
                        stack.append(action(stack.pop(), stack.pop()))
                    elif token == '*':
                        action = lambda x, y: y * x
                        stack.append(action(stack.pop(), stack.pop()))
                    elif token == '/':
                        action = lambda x, y: y / x
                        stack.append(action(stack.pop(), stack.pop()))
                    elif token == '~':
                        action = lambda x: x * -1
                        stack.append(action(stack.pop()))
                else:
                    stack.append(self.cast(token))

        except IndexError as e:
            message = 'Too few arguments'
            raise MalformedTermException(message)

        if len(stack) == 0:
            raise MalformedTermException('Term is empty')
        elif len(stack) > 1:
            raise MalformedTermException('Excess arguments')
        else:
            return stack[0]


    def cast(self, value):
        """
        Cast an int or float in a string to the correct type to be
        able to run mathematical operators on it
        """
        return float(value) if '.' in value else int(value)

