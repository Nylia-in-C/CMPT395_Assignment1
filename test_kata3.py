#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 3

#Program Purpose: TDD Testing for Kata 1

import kata3 as k3
import pytest

#Tests pass_valid function
class Test_pass_val:
    #1: Check for string length of 8 (True)
    def test1(self):
        (is_valid, err_msg) = k3.pass_val("12345678")
        assert is_valid == "True"
        assert err_msg == ""
    #2: Check for string length of 8 (False)
    def test2(self):
        (is_valid, err_msg) = k3.pass_val("123456")
        assert is_valid == "False"
        assert err_msg == "Password must be at least 8 characters"    
