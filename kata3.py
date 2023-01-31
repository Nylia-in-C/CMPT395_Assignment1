#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 3

#Purpose:       Validates passwords according to these specs:
#               - At least 8 characters long
#               - At least 2 numbers, 1 capital letter, 1 special character
#Parameters:    string - password to be validated
#Return:        is_valid - Bool for password validity
#               err_msg - string indicating why password is not valid

#Note: Due to being a password function, the default fail-safe is to
#return false unless every check passes. This results in longer code
#but better complies with secure coding logic.

def pass_val(string):

    #Initializations
    is_valid = False
    err_msg = ""

    #count numbers and capital letters in string
    countN = countU = countS = 0 #initialize num, UC, special counter
    for char in string:
        if char.isdigit() == True:
            countN += 1
        elif char.isupper() == True:
            countU += 1
        elif char.isalnum() == False:
            countS += 1

    #string length of min 8
    if len(string) >= 8: 
        is_min8 = True
    else:
        is_min8 = False
        err_msg+=("Password must be at least 8 characters\n")
    
    #minimum 2 numbers
    if (countN >= 2):
        has_2nums = True
    else:
        has_2nums = False
        err_msg+=("The password must contain at least 2 numbers\n")

    #minimum 1 capital letter
    if (countU >= 1):
        has_upper = True
    else:
        has_upper = False
        err_msg+=("Password must contain at least one capital letter\n")

    #minimum 1 special character
    if (countS >= 1):
        has_special = True
    else:
        has_special = False
        err_msg+=("Password must contain at least one special character\n")

    #check if all flags are true
    if (is_min8 and has_2nums and has_upper and has_special): 
        is_valid = True

    err_msg = err_msg[0:-1] #remove final \n
    return (is_valid, err_msg)
