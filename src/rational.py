class Rational(object):

    def __init__(self, num_, denom_):
        assert int(num_) - num_ == int(denom_) - denom_ == 0 and int(denom_) > 0
        self.sign = -1 if int(num_) < 0 else 1
        num, denom = abs(int(num_)), abs(int(denom_))
        self.int = num//denom
        self.num, self.denom = self.simplify(num - self.int*denom, denom)

    def __str__(self):
        pattern = '(-{})' if self.sign == -1 else '{}'
        if self.int:
            if self.num:
                number_str = '{} {}/{}'.format(self.int, self.num, self.denom)
            else:
                number_str = '{}'.format(self.int)
        else:
            number_str = '{}/{}'.format(self.num, self.denom)
        return pattern.format(number_str)

    def __add__(self, other):
        assert isinstance(other, self.__class__)
        num1, denom1 = self.as_fraction()
        num2, denom2 = other.as_fraction()
        num = num1*denom2 + num2*denom1
        denom = denom1*denom2
        return self.__class__(num, denom)

    def __mul__(self, other):
        assert isinstance(other, self.__class__)
        num1, denom1 = self.as_fraction()
        num2, denom2 = other.as_fraction()
        num = num1*num2
        denom = denom1*denom2
        return self.__class__(num, denom)

    def __sub__(self, other):
        assert isinstance(other, self.__class__)
        return self + self.__class__(-1, 1)*other
        

    def __div__(self, other):
        assert isinstance(other, self.__class__)
        num1, denom1 = self.as_fraction()
        num2, denom2 = other.as_fraction()
        if num2 == 0:
            raise ZeroDivisionError
        denom = denom1*num2
        num = num1*denom2 if denom > 0 else -num1*denom2
        return self.__class__(num, abs(denom))

    def as_fraction(self):
        return (self.sign*(self.int*self.denom + self.num), self.denom)

    @staticmethod
    def simplify(num_, denom_):
        num, denom = num_, denom_
        coef = 2
        while coef <= num:
            if num%coef == 0 and denom%coef == 0:
                num, denom = num/coef, denom/coef
                if num == 1:
                    break
            else:
                coef += 1
        return num, denom
