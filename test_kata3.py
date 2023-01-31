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
        (is_valid, err_msg) = k3.pass_val("A12345678")
        assert is_valid == True
        assert err_msg == ""
    #2: Check for string length of 8 (False)
    def test2(self):
        (is_valid, err_msg) = k3.pass_val("A123456")
        assert is_valid == False
        assert err_msg == "Password must be at least 8 characters"

    #3: Check for minimum 2 numbers (True)
    def test3(self):
        (is_valid, err_msg) = k3.pass_val("A12345678")
        assert is_valid == True
        assert err_msg == ""    
    #4: Check for minimum 2 numbers (False)
    def test4(self):
        (is_valid, err_msg) = k3.pass_val("Abcdefghijklm1")
        assert is_valid == False
        assert err_msg == "The password must contain at least 2 numbers"

    #5: Check for multiple error messages
    def test5(self):
        (is_valid, err_msg) = k3.pass_val("pAsswd")
        assert is_valid == False
        assert err_msg == ("Password must be at least 8 characters\n"
        "The password must contain at least 2 numbers")            

    #6: Check for uppercase (True)
    def test6(self):
        (is_valid, err_msg) = k3.pass_val("A1234567")
        assert is_valid == True
        assert err_msg == ""
    #7: Check for uppercase (False)
    def test7(self):
        (is_valid, err_msg) = k3.pass_val("a1234567")
        assert is_valid == False
        assert err_msg == "Password must contain at least one capital letter"
    