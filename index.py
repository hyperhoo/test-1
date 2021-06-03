from unittest import TestCase
import unittest


class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime-1
            )
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not(self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    # 연습문제 1.6
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        num = (self.num ** exponent) % self.prime
        return self.__class__(num, self.prime)


class FieldElementTest(TestCase):

    # page 42
    def test1(self):
        a = FieldElement(7, 13)
        b = FieldElement(6, 13)
        print(a == b)
        print(a == a)

    # page 49
    def test2(self):
        a = FieldElement(7, 13)
        b = FieldElement(12, 13)
        c = FieldElement(6, 13)
        print(a+b == c)

    # 연습문제 1.4
    def test3(self):
        prime = 97
        print((95 * 45 * 31) % prime)
        print((17 * 13 * 19 * 44) % prime)
        print((12**7 * 77**49) % prime)

    # 연습문제 1.5
    def test4(self):
        prime = 19
        k = [1, 3, 7, 13, 18]
        member = []
        for i in k:
            for j in range(0, 19):
                member.append((i*j) % prime)
            member.sort()
            print(member)
            member.clear()

    # page 50
    def test5(self):
        a = FieldElement(3, 13)
        b = FieldElement(1, 13)
        print(a**3 == b)

    # 연습문제 1.7 - 서정훈 풀이
    def test6(self):
        p = 7
        member = []
        for j in range(1, 7):
            member.append((j**(7-1)) % 7)
        member.sort()
        print(member)
        member.clear()

        p = 11
        member = []
        for j in range(1, 11):
            member.append((j**(11-1)) % 11)
        member.sort()
        print(member)
        member.clear()

        p = 17
        member = []
        for j in range(1, 17):
            member.append((j**(17-1)) % 17)
        member.sort()
        print(member)
        member.clear()

        p = 31
        member = []
        for j in range(1, 31):
            member.append((j**(31-1)) % 31)
        member.sort()
        print(member)
        member.clear()

    # 연습문제 1.7 - 책 해답
    def test7(self):
        for prime in (7, 11, 17, 31):
            print([pow(i, prime-1, prime) for i in range(1, prime)])

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # runner.run(unittest.makeSuite(FieldElementTest, 'test6'))
    runner.run(unittest.makeSuite(FieldElementTest, 'test7'))
    
