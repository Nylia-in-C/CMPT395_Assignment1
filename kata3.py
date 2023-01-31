#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 3

#Purpose:       Validates passwords according to these specs:
#               - At least 8 characters long
#Parameters:    string - password to be validated
#Return:        is_valid - Bool for password validity
#               err_msg - string indicating why password is not valid

def pass_val(string):
    if (len(string) < 8):
        err_msg = "Password must be at least 8 characters"
        return (False, err_msg)
    return (True, "")