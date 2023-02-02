#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 1

#Purpose:       Accepts a number as input and returns a string
#               Returns "Fizz" for multiples of 3
#               Returns "Buzz" for multiples of 5
#               Returns "FizzBuzz" if multiple of both 3 and 5
#Parameters:    num: integer to be converted
#Return:        string: String representing the entered number
#                       or "FizzBuzz"/"Fizz"/"Buzz" for special
#                       cases outlined in Purpose

def fizzbuzz(num):
    if ((num % 3 == 0) and (num % 5 == 0)):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    return(str(num))

#verbose print testing
if __name__ == "__main__":
    inputs = [1, 8, -5344, 3, 999, -63, 5, 50, -25, 15, 45, -300]

    for num in inputs:
        print("Input: \t", num, "\tOutput: ", fizzbuzz(num))