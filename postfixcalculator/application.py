#!/usr/bin/env python3

from postfixcalculator.calculator.postfixcalculator import PostFixCalculator

def main():
    calculator = PostFixCalculator()
    term = ''
    while True:
        print('\nPlease enter your postfix calculation or q to quit')
        term = input('> ').strip()  # get rid of whitespace

        if term == 'q':
            break

        result = calculator.calculate(term)
        print('The result is %s' %result)


if __name__ == '__main__':
    main()