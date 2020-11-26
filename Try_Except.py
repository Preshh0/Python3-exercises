'''
    number = int(input("Enter a number: "))
    print(number)
'''

#a try except block enables a program to try out a piece of code.
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")