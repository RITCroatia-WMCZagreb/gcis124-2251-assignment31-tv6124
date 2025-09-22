'''
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''
import math 
def fact(x):
    if x>0:
        return math.factorial(x)
    else:
        return 0

def root(x):
    if x>0:
        return math.sqrt(x)
    else:
        return 0
    
def trunk(x):
    return math.trunc(x)
    
def main():
   number=float(input("Enter a numeric value: "))
   print(number, "factorial = ", fact(int(number)))
   print("The square root of ", number, "=", root(number))
   number_2=float(input("Enter a numeric value: "))
   print(number_2, "truncated = ", trunk(number_2))



if __name__ == "__main__":
    main()