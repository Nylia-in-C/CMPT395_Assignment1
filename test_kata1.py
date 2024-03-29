#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 1

#Program Purpose: TDD Testing for Kata 1

import kata1 as k1
import pytest

#Tests fizzbuzz (kata1) to see if nums converted to str
class Test_fizzbuzz:
    #1-3: Check basic conversion functionality
    def test1(self):
        str = k1.fizzbuzz(1)
        assert str == "1"

    def test2(self):
        str = k1.fizzbuzz(8)
        assert str == "8"

    def test3(self):
        str = k1.fizzbuzz(-534544)
        assert str == "-534544"

    #4-6: Check if multiples of 3 return "Fizz" instead
    def test4(self):
        str = k1.fizzbuzz(3)
        assert str == "Fizz"

    def test5(self):
        str = k1.fizzbuzz(999)
        assert str == "Fizz"

    def test6(self):
        str = k1.fizzbuzz(-63)
        assert str == "Fizz"

    #7-9: Check if multiples of 5 return "Buzz" instead
    def test7(self):
        str = k1.fizzbuzz(5)
        assert str == "Buzz"

    def test8(self):
        str = k1.fizzbuzz(50)
        assert str == "Buzz"

    def test9(self):
        str = k1.fizzbuzz(-25)
        assert str == "Buzz"

    #10-12: Multiples of 3 AND 5 return "FizzBuzz"
    def test10(self):
        str = k1.fizzbuzz(15)
        assert str == "FizzBuzz"

    def test11(self):
        str = k1.fizzbuzz(45)
        assert str == "FizzBuzz"

    def test12(self):
        str = k1.fizzbuzz(-300)
        assert str == "FizzBuzz"
