#####################################################
__author__ = "VIGNESH"
__copyright__ = "Copyright (C) 2024 Author Vignesh"
__license__ = "Public"
__version__ = "1.0"
#####################################################

#########
import re
#########

password = input("Enter a Password To check weather it is valid or Not:")
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
if flag ==-1:
    print("Not a Valid Password")
