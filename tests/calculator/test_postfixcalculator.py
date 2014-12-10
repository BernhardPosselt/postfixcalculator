#!/usr/bin/env python3

import unittest

from postfixcalculator.calculator.postfixcalculator import PostFixCalculator, MalformedTermException


class PostfixCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = PostFixCalculator()

    def test_sanity(self):
        self.assertEqual(3, 3)


    def test_simple_addition(self):
        term = '1 2 +'
        result = self.calculator.calculate(term)

        self.assertEqual(3, result)


    def test_simple_addition2(self):
        term = '2 3 +'
        result = self.calculator.calculate(term)

        self.assertEqual(5, result)


    def test_ignore_too_much_whitespace(self):
        term = '2  3  + '
        result = self.calculator.calculate(term)

        self.assertEqual(5, result)


    def test_negative_addition(self):
        term = '2 -3 +'
        result = self.calculator.calculate(term)

        self.assertEqual(-1, result)


    def test_subtraction(self):
        term = '2 3 -'
        result = self.calculator.calculate(term)

        self.assertEqual(-1, result)


    def test_negative_subtraction(self):
        term = '-2 -3 -'
        result = self.calculator.calculate(term)

        self.assertEqual(1, result)

    def test_multiplication(self):
        term = '-2 -3 *'
        result = self.calculator.calculate(term)

        self.assertEqual(6, result)


    def test_division(self):
        term = '6 2 /'
        result = self.calculator.calculate(term)

        self.assertEqual(3, result)


    def test_no_whitespace(self):
        term = '3 4 5 +*'
        result = self.calculator.calculate(term)

        self.assertEqual(27, result)


    def test_no_result(self):
        term = ''
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term(self):
        term = '3 4 5 +**'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


if __name__ == '__main__':
    unittest.main()