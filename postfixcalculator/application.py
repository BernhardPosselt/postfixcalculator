#!/usr/bin/env python3

from postfixcalculator.calculator.postfixcalculator import PostFixCalculator, MalformedTermException

def main():
    calculator = PostFixCalculator()
    term = ''
    while True:
        print('\nPlease enter your postfix calculation or q to quit')
        term = input('> ').strip()  # get rid of whitespace

        if term == 'q':
            break

        try:
            result = calculator.calculate(term)
            print('The result is %s' %result)
        except MalformedTermException as e:
            print(e)


if __name__ == '__main__':
    main()