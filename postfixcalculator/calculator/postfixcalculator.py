import re


class PostFixCalculator:

    def calculate(self, term):
        stack = []
        term = list(term)  # convert term to list so we can call pop on it

        token = self.pop_next_token(term)

        while token != None:
            # sometimes the next token is needed e.g. unary - or +
            next_token = self.get_next_token(term)

            # unary minus and plus
            if token in '+-' and next_token and next_token.isdigit():
                token = token + self.pop_next_token(term)
                token = self.cast(token)
                stack.append(token)

            elif token.isdigit():
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

            token = self.pop_next_token(term)

        return stack[0]


    def pop_next_token(self, term):
        """
        Get the next token that is not a white space character and remove
        it from the list
        """
        while len(term) > 0:
            token = term.pop(0)  # pop at position 0
            if token != ' ':
                return token
        return None


    def get_next_token(self, term):
        """
        Peak ahead and return the next token without removing it from the term
        """
        for token in term:
            if token != ' ':
                return token
        return None


    def cast(self, value):
        """
        Cast an int or float in a string to the correct type to be
        able to run mathematical operators on it
        """
        return float(value) if '.' in value else int(value)

