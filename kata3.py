#Selena Weber
#3126501
#CMPT395 AS02
#Assignment 1, Kata 3

#Purpose:       Validates passwords according to these specs:
#               - At least 8 characters long
#Parameters:    string - password to be validated
#Return:        is_valid - Bool for password validity
#               err_msg - string indicating why password is not valid

#Note: Due to being a password function, the default fail-safe is to
#return false unless every check passes. This results in longer code
#but better complies with secure coding logic.

def pass_val(string):
    if (len(string) >= 8): #string length of min 8
        is_min8 = True
    else:
        err_msg = "Password must be at least 8 characters"
        return (False, err_msg)
    

    if (is_min8 == True): #check if all flags are true
        return (True, "")

    else:
        return (False, err_msg)

if __name__ == "__main__":
    pass_val("testing1234")