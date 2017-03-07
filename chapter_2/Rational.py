class Rational():
    @staticmethod
    def _gcd(m, n):
        if n==0:
            m, n = n, m
        while m != 0:
            m, n = n%m , m
        return n
    def __init__(self, num, den=1):
        assert isinstance(num,int) and isinstance(den, int), "分子分母必须是整数"
        if den == 0: raise ZeroDivisionError
        sign = 1
        if num < 0:
            num *= -1
            sign *= -1
        if den < 0:
            den *= -1
            sign *= -1
        g = Rational._gcd(num, den)
        self._num = sign * (num // g)
        self._den = den // g
    def num(self):
        return self._num
    def den(self):
        return self._den
    def __add__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
            raise TypeError("请输入整数或有理数")
        den = self._den * other.den()
        num = self._num * other.den() + self._den * other.num()
        return Rational(num, den)
    def __radd__(self, other):
        return self + other
    def __mul__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
            raise TypeError("请输入整数或有理数")
        return Rational(self._num * other.num(), self._den * other.den())
    def __floordiv__(self, other):
        if other is 0:
            raise ZeroDivisionError
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
            raise TypeError("请输入整数或有理数")
        return Rational(self._num * other.den(), self._den * other.num())
    def __truediv__(self, other):
        return self//other
    def __sub__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        den = self._den * other.den()
        num = self._num * other.den() - self._den * other.num()
        return Rational(num, den)
    def __eq__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return self._num * other.den() == self._den * other.num()
    def __lt__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return self._num * other.den() < self._den * other.num()
    def __ne__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return self._num * other.den() != self._den * other.num()
    def __le__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return self._num * other.den() <= self._den * other.num()
    def __gt__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return self._num * other.den() > self._den * other.num()
    def __ge__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return self._num * other.den() >= self._den * other.num()
    def __rsub__(self, other):
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
        return other - self
    def __str__(self):
        return '%s/%s' %(self._num,self._den)

if __name__ == '__main__':
    x = Rational(2,4)
    print(x)
    y = Rational(1,3)
    print(1 - x)
    print(x - 1)
    print(y*x)
    print(x/y)
