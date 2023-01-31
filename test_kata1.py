#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 1

#Program Purpose: TDD Testing for Kata 1

import kata1 as k1
import pytest

class Test_num2str:
    def test1(self):
        str = k1.num2str(1)
        assert str == "1"

    def test2(self):
        str = k1.num2str(10)
        assert str == "10"

    def test3(self):
        str = k1.num2str(-534544)
        assert str == "-534544"