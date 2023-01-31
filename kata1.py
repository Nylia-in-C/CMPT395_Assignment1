#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 1

#Program Purpose: [WIP] I'll know when the kata is done I guess?

#Purpose:       Accepts a number as input and returns a string
#               Returns "Fizz" for multiples of 3
#Parameters:    num: integer to be converted
#Return:        string: String representing the entered number
#                       or "Fizz" for multiples of 3
def fizzbuzz(num):
    if ((num % 3 == 0) and (num % 5 == 0)):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    return(str(num))

