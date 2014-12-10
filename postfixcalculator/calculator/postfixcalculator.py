import re

class MalformedTermException(Exception):
    pass


class PostFixCalculator:

    def calculate(self, term):
        stack = []
        original_term = ''.join(term)  # copy string for error message
        term = list(term)  # convert term to list so we can call pop on it
        exec_position = 0  # position for getting the error hint

        try:
            token, steps = self.pop_next_token(term)

            while token:
                exec_position += steps

                # sometimes the next token is needed e.g. unary - or +
                next_token = self.get_next_token(term)

                # unary minus and plus
                if token in '+-' and next_token and self.is_number(next_token) \
                and len(stack) < 2:
                    next_token, steps = self.pop_next_token(term)
                    exec_position += steps
                    token = token + next_token
                    token = self.cast(token)
                    stack.append(token)

                elif self.is_number(token):
                    token = self.cast(token)
                    stack.append(token)

                elif token in '+-/*':
                    action = None
                    if token == '+':
                        action = lambda x, y: y + x # pop reverses the order
                    elif token == '-':
                        action = lambda x, y: y - x
                    elif token == '*':
                        action = lambda x, y: y * x
                    elif token == '/':
                        action = lambda x, y: y / x
                    stack.append(action(stack.pop(), stack.pop()))

                token, steps = self.pop_next_token(term)

        except IndexError as e:
            message = 'Malformed expression at position %d\n' % exec_position
            message += '%s\n' % original_term
            message += ' ' * (exec_position - 1) + '^'
            raise MalformedTermException(message)

        if len(stack) == 0:
            raise MalformedTermException('Term is empty')
        elif len(stack) > 1:
            raise MalformedTermException('Excess arguments')
        else:
            return stack[0]


    def pop_next_token(self, term):
        """
        Get the next token that is not a white space character and remove
        it from the list and the number of steps it took to get it to
        provide debug information
        """
        steps = 0
        while len(term) > 0:
            steps += 1
            token = term.pop(0)  # pop at position 0

            if token == ' ':
                continue
            else:
                next_token = self.get_next_token(term, True)

                # assemble longer numbers
                while token.isdigit() and next_token and next_token.isdigit():
                    token += term.pop(0)
                    next_token = self.get_next_token(term, True)
                    steps += 1

                # float support
                next_token = self.get_next_token(term, True)
                if next_token == ' ':
                    term.pop(0)
                    steps += 1
                elif next_token == '.':
                    # append .
                    next_token = term.pop(0)
                    token += next_token
                    steps += 1

                    # append following number
                    next_token, stepsn = self.pop_next_token(term)
                    token += next_token
                    steps += stepsn

                return token, steps

        return None, steps


    def is_number(self, value):
        return re.match(r'(\d+)|(\d+\.\d+)', value)


    def get_next_token(self, term, tokenize_whitespace=False):
        """
        Peak ahead and return the next token without removing it from the term
        """
        for token in term:
            if tokenize_whitespace:
                return token
            elif token != ' ':
                return token
        return None


    def cast(self, value):
        """
        Cast an int or float in a string to the correct type to be
        able to run mathematical operators on it
        """
        return float(value) if '.' in value else int(value)

