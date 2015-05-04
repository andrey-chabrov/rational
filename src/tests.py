import unittest

from . import rational


class TestRational(unittest.TestCase):

    def test_init(self):

        test_list = (
            ((1, 3), '1/3'),
            ((-1, 3), '(-1/3)'),
            ((0, 3), '0/3'),
            ((3, 3), '1'),
            ((5, 3), '1 2/3'),
            ((-160, 120), '(-1 1/3)'),
        )

        for number, result in test_list:
            rat = rational.Rational(*number)
            self.assertEquals(result, str(rat))

    def test_wrong_input(self):
        self.assertRaises(ValueError, rational.Rational, *(1, '1.5'))
        self.assertRaises(AssertionError, rational.Rational, *(1.5, 1.5))
        self.assertRaises(ValueError, rational.Rational, *('abc', 1))
        self.assertRaises(AssertionError, rational.Rational, *(1, -1))

    def test_add(self):

        test_list = (
            (((1, 3), (2, 3)), '1'),
            (((-1, 3), (2, 3)), '1/3'),
            (((-5, 1), (7, 4)), '(-3 1/4)'),
            (((1, 5), (2, 3)), '13/15'),
            (((-60, 120), (40, 14)), '2 5/14'),
            (((-0, 120), (0, 10)), '0/1200'),
        )

        for nums, result in test_list:
            a_, b_ = nums
            a, b = rational.Rational(*a_), rational.Rational(*b_)
            self.assertEquals(str(a + b), result)

    def test_add_wrong_arg(self):
        self.assertRaises(AssertionError, rational.Rational(2, 3).__add__, 123)

    def test_mul(self):

        test_list = (
            (((1, 3), (2, 3)), '2/9'),
            (((-1, 3), (2, 3)), '(-2/9)'),
            (((-5, 1), (-7, 4)), '8 3/4'),
            (((1, 5), (2, 3)), '2/15'),
            (((-60, 120), (40, 14)), '(-1 3/7)'),
            (((-0, 120), (0, 10)), '0/1200'),
            (((-1, 1), (2, 10)), '(-1/5)'),
        )

        for nums, result in test_list:
            a_, b_ = nums
            a, b = rational.Rational(*a_), rational.Rational(*b_)
            self.assertEquals(str(a*b), result)

    def test_mul_wrong_arg(self):
        self.assertRaises(AssertionError, rational.Rational(2, 3).__mul__, 123)

    def test_div(self):

        test_list = (
            (((1, 3), (2, 3)), '1/2'),
            (((-1, 3), (2, 3)), '(-1/2)'),
            (((-5, 1), (-7, 4)), '2 6/7'),
            (((-60, 120), (40, 14)), '(-7/40)'),
            (((-0, 120), (1, 10)), '0/120'),
            (((-1, 1), (2, 10)), '(-5)'),
        )

        for nums, result in test_list:
            a_, b_ = nums
            a, b = rational.Rational(*a_), rational.Rational(*b_)
            self.assertEquals(str(a/b), result)

    def test_div_wrong_arg(self):
        self.assertRaises(AssertionError, rational.Rational(2, 3).__div__, 123)
        self.assertRaises(ZeroDivisionError,
            rational.Rational(2, 3).__div__,
            rational.Rational(0, 3))

    def test_sub(self):

        test_list = (
            (((1, 3), (2, 3)), '(-1/3)'),
            (((-1, 3), (2, 3)), '(-1)'),
            (((-5, 1), (-7, 4)), '(-3 1/4)'),
            (((-60, 120), (40, 14)), '(-3 5/14)'),
            (((-0, 120), (1, 10)), '(-1/10)'),
            (((1, 1), (2, 10)), '4/5'),
        )

        for nums, result in test_list:
            a_, b_ = nums
            a, b = rational.Rational(*a_), rational.Rational(*b_)
            self.assertEquals(str(a - b), result)

    def test_sub_wrong_arg(self):
        self.assertRaises(AssertionError, rational.Rational(2, 3).__sub__, 123)


if __name__ == '__main__':
    unittest.main()
