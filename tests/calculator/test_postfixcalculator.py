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


    def test_subtraction_big_numbers(self):
        term = '23 32 -'
        result = self.calculator.calculate(term)

        self.assertEqual(-9, result)


    def test_negative_subtraction(self):
        term = '-2 -3 -'
        result = self.calculator.calculate(term)

        self.assertEqual(1, result)


    def test_multiplication(self):
        term = '-2 -3 *'
        result = self.calculator.calculate(term)

        self.assertEqual(6, result)


    def test_floats(self):
        term = '1.5 2.5 +'
        result = self.calculator.calculate(term)

        self.assertEqual(4.0, result)


    def test_division(self):
        term = '6 2 /'
        result = self.calculator.calculate(term)

        self.assertEqual(3, result)


    def test_no_whitespace(self):
        term = '3 4 5 +*'
        result = self.calculator.calculate(term)

        self.assertEqual(27, result)


    def tes_complex_term(self):
        term = '3 4 + 5 6 + *'
        result = self.calculator.calculate(term)

        self.assertEqual(77, result)


    def test_no_result(self):
        term = ''
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term(self):
        term = '3 4 5 +**'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term2(self):
        term = '3 4 5 4 + +'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_pop_next_simple_token(self):
        term = list('345')
        token, position = self.calculator.pop_next_token(term)
        self.assertEqual(3, position)
        self.assertEqual('345', token)


    def test_pop_next_token(self):
        term = list('345 323')
        token, position = self.calculator.pop_next_token(term)
        self.assertEqual(4, position)
        self.assertEqual('345', token)
        self.assertEqual(list('323'), term)


    def test_pop_next_token_float(self):
        term = list('1.423 3')
        token, position = self.calculator.pop_next_token(term)
        self.assertEqual(6, position)
        self.assertEqual('1.423', token)
        self.assertEqual(list('3'), term)

    def test_pop_next_token_floats(self):
        term = list('1.423 3.4')
        token, position = self.calculator.pop_next_token(term)
        next_token, next_position = self.calculator.pop_next_token(term)
        self.assertEqual(6, position)
        self.assertEqual('1.423', token)
        self.assertEqual(3, next_position)
        self.assertEqual('3.4', next_token)


    def test_get_next_token(self):
        term = list(' 1.423')
        token = self.calculator.get_next_token(term)
        self.assertEqual('1', token)


    def test_get_next_token_whitespace(self):
        term = list(' 1.423')
        token = self.calculator.get_next_token(term, True)
        self.assertEqual(' ', token)


    def test_get_next_token_no_token(self):
        term = list('')
        token = self.calculator.get_next_token(term, True)
        self.assertEqual(None, token)



if __name__ == '__main__':
    unittest.main()