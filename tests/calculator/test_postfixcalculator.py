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
        term = '2 3 ~ +'
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
        term = '2 ~ 3 -'
        result = self.calculator.calculate(term)

        self.assertEqual(-5, result)


    def test_multiplication(self):
        term = '2 3 *'
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


    def test_complex_term(self):
        term = '3 4 + 5 6 + *'
        result = self.calculator.calculate(term)

        self.assertEqual(77, result)


    def test_complex_unary_term(self):
        term = '3 4 ~ 5 - *'
        result = self.calculator.calculate(term)

        self.assertEqual(-27, result)


    def test_no_result(self):
        term = ''
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term_parameters(self):
        term = '3 4'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term_few_parameters(self):
        term = '3 4 5 +**'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term_unkown_token(self):
        term = '3 a 5 +*'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_malformed_term3_excess_arguments(self):
        term = '3 4 5 4 + +'
        self.assertRaises(MalformedTermException, self.calculator.calculate, term)


    def test_negation(self):
        term = '4 ~'
        result = self.calculator.calculate(term)
        self.assertEqual(-4, result)


    def test_double_negation(self):
        term = '4 ~~'
        result = self.calculator.calculate(term)
        self.assertEqual(4, result)


    def test_tokenize(self):
        term = '4 3'
        result = self.calculator.tokenize(term)
        self.assertEqual(['4', '3'], result)


    def test_tokenize_big_number(self):
        term = '4 34'
        result = self.calculator.tokenize(term)
        self.assertEqual(['4', '34'], result)

if __name__ == '__main__':
    unittest.main()