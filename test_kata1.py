#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 1

#Program Purpose: TDD Testing for Kata 1

import kata1 as k1
import pytest

#Tests fizzbuzz to see if nums converted to str
class Test_fizzbuzz:
    def test1(self):
        str = k1.fizzbuzz(1)
        assert str == "1"

    def test2(self):
        str = k1.fizzbuzz(10)
        assert str == "10"

    def test3(self):
        str = k1.fizzbuzz(-534544)
        assert str == "-534544"