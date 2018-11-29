####################################
# => G E N E S I S <=              #
# By S4n1x D4rk3r                  #
# https://github.com/Sanix-Darker  #
# PYTHON-CAMEROUN                  #
####################################

import os
from itertools import combinations 
  

print "\n|-----------------------------------"
print "| => G E N E S I S <=              |"
print "| By S4n1x D4rk3r                  |"
print "| https://github.com/Sanix-Darker  |"
print "| PYTHON-CAMEROUN                  |"
print "====================================\n"

# The link of the website
# keys = raw_input("\nEnter key words seperate by \",\" (Ex: manioc, patate):")

keys = "sdcds,sdc"
# Superfux
Superfux = ['A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z','a','b','c','d',
            'e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x',
            'y','z',';',',','.','0','1','2','3','4',
            '5','6','7','8','9','!','@','#','$','%',
            '^','&','*','/','<','>','|',']','[','}',
            '{']
# array Keys
array_keys = keys.split(',')

# Open the password file
file_password = open("passwords.txt", "w+");

# loop throught possibilities 
# Python function to print permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  
# Driver program to test above function 
data = list('123') 
for p in permutation(data):
    file_password.write(p+"\n")
    print p

# Pause the console
os.system("pause")