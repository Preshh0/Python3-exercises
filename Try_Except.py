'''
    number = int(input("Enter a number: "))
    print(number)
'''

#a try except block enables a program to try out a piece of code.
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
    
#it is important to state the type of error and what to print for it respectively. Not doing so will mean the user won't be able to tell exactly what error is being experienced.
#best practice in python is to indicate specific errors.
except ZeroDivisionError as err: #using "as" helps you print out exactly what the error was without you having to type it in the print function.
    print(err)
except ValueError:
    print("Invalid Input")
    
    
    